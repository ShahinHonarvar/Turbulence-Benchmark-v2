from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[70]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result) if result else []

def is_left_right_truncatable_prime(num):
    if not isprime(num):
        return False
    digits = len(str(num))
    for i in range(2, digits + 1):
        if not isprime(num % 10 ** (i - 1)) or not isprime(num // 10 ** (i - 1)):
            return False
    return True