def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[42]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        left_trunc = num
        right_trunc = num
        while left_trunc > 0:
            if not is_prime(left_trunc):
                is_truncatable = False
                break
            left_trunc //= 10
        while right_trunc > 0:
            if not is_prime(right_trunc):
                is_truncatable = False
                break
            right_trunc = int(str(right_trunc)[:-1]) if right_trunc > 9 else right_trunc
            if right_trunc == 0:
                break
        if is_truncatable:
            result.append(num)
    return sorted(result)