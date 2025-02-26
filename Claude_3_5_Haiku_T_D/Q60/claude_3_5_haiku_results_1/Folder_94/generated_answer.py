def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n))):
        left_trunc = int(str(n)[i:])
        right_trunc = int(str(n)[:len(str(n)) - i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(nums):
    x = nums[43]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)