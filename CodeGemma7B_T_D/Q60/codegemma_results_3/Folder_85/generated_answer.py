from sympy import isprime

def is_truncatable_prime(n):
    if n <= 1 or n % 2 == 0 or '0' in str(n):
        return False
    for i in range(len(str(n)) - 1):
        left = int(str(n)[:-i - 1])
        right = int(str(n)[i + 1:])
        if not isprime(left) or not isprime(right):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[94]
    result = []
    for n in range(2, x + 1):
        if is_truncatable_prime(n):
            result.append(n)
    return sorted(result) or []