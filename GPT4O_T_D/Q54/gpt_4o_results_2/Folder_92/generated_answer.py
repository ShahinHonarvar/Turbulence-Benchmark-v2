from sympy import isprime

def all_right_truncatable_prime(nums):
    if len(nums) <= 7:
        return []
    x = nums[7]

    def is_right_truncatable_prime(n):
        trunc = str(n)
        while trunc:
            if not isprime(int(trunc)):
                return False
            trunc = trunc[:-1]
        return True
    result = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(result)