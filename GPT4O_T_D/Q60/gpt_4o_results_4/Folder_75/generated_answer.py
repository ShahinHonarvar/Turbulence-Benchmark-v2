from sympy import isprime

def all_left_right_truncatable_prime(nums):

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:len(s) - i])):
                return False
        return True
    x = nums[41]
    return sorted((n for n in range(10, x + 1) if is_truncatable_prime(n)))