from sympy import isprime

def all_left_right_truncatable_prime(n):

    def is_truncatable_prime(num):
        while num > 10:
            if not isprime(num):
                return False
            num = int(str(num)[1:]) if num % 10 != 0 else 0
        return True
    primes = [i for i in range(2, n + 1) if isprime(i)]
    left_right_primes = [i for i in primes if is_truncatable_prime(i)]
    return sorted(set(left_right_primes))