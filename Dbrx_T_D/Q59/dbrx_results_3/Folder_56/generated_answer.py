from sympy import isprime

def all_left_truncatable_prime(nums):

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True
    x = nums[29]
    return [i for i in range(1, x) if is_left_truncatable_prime(i) and i != 1]