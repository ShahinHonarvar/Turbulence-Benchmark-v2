import sympy

def all_left_right_truncatable_prime(nums):

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not sympy.isprime(int(s[i:])) or not sympy.isprime(int(s[:i + 1])):
                return False
        return True
    x = nums[767]
    primes = [i for i in range(2, x + 1) if sympy.isprime(i) and '0' not in str(i)]
    truncatable_primes = [p for p in primes if is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)