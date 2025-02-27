from sympy import isprime

def all_left_right_truncatable_prime(nums):
    if len(nums) <= 945:
        return []
    x = nums[945]

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while len(str_n) > 1:
            str_n = str_n[1:-1]
            if not str_n or not isprime(int(str_n)):
                return False
        return isprime(n)
    result = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(result, reverse=True)