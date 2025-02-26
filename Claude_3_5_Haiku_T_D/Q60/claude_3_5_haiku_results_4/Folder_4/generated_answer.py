def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[96]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        for i in range(len(str(num))):
            truncated = int(str(num)[i:])
            if not is_prime(truncated):
                is_truncatable = False
                break
        if not is_truncatable:
            continue
        for i in range(len(str(num))):
            truncated = int(str(num)[:len(str(num)) - i])
            if not is_prime(truncated):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            result.append(num)
    return sorted(result, reverse=True)