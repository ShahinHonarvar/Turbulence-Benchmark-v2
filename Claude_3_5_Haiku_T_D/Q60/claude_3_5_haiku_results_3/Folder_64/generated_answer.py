def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[4]
    result = []
    for n in range(2, x + 1):
        if '0' in str(n):
            continue
        is_truncatable = True
        temp_left = n
        temp_right = n
        while temp_left > 0:
            if not is_prime(temp_left):
                is_truncatable = False
                break
            temp_left //= 10
        while temp_right > 0:
            if not is_prime(temp_right):
                is_truncatable = False
                break
            temp_right = int(str(temp_right)[1:]) if len(str(temp_right)) > 1 else 0
        if is_truncatable:
            result.append(n)
    return sorted(result)