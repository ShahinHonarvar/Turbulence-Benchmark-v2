from sympy import isprime

def all_left_right_truncatable_prime(nums):

    def is_truncatable_prime(n):
        if n < 10 and isprime(n):
            return True
        while n > 0:
            if not isprime(n) or '0' in str(n):
                return False
            n = int(str(n)[:-1]) if n > 9 else 0
        return n == 0 or isprime(n)
    return sorted((x for x in nums if is_truncatable_prime(x) and x <= nums[86]))