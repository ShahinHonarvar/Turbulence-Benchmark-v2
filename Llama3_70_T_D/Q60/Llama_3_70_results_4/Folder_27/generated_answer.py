import sympy

def all_left_right_truncatable_prime(nums):
    x = nums[79]

    def is_left_right_truncatable_prime(n):
        if n < 10:
            return sympy.isprime(n)
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not sympy.isprime(int(str_n[i:])) or not sympy.isprime(int(str_n[:-i])):
                return False
        return True
    truncatable_primes = [i for i in range(x, 7, -1) if sympy.isprime(i) and is_left_right_truncatable_prime(i)]
    return truncatable_primes