from sympy import isprime

def all_left_right_truncatable_prime(nums):

    def is_left_right_truncatable(n):
        if not 1 < n < 10:
            return False
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:]) if n < 10 else int(str(n)[:-1])
        return True
    return sorted(filter(is_left_right_truncatable, range(1, nums[30] + 1)))