import sympy

def all_right_truncatable_prime(nums):
    if len(nums) <= 96:
        return []
    x = nums[96]

    def is_right_truncatable_prime(n):
        k = n
        while k > 0:
            if not sympy.isprime(k):
                return False
            k //= 10
        return True
    result = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(result, reverse=True)