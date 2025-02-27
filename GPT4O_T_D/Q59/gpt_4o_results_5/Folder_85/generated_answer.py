from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[94]
    result = []

    def is_left_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        while s:
            if not isprime(int(s)):
                return False
            s = s[1:]
        return True
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return result