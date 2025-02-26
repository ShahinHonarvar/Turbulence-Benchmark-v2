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
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
        if n > 0 and (not is_prime(n)):
            return False
    s = str(n)
    while len(s) > 0:
        if not is_prime(int(s)):
            return False
        s = s[1:]
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[630]
    result = []
    for num in range(x, 11, -1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result