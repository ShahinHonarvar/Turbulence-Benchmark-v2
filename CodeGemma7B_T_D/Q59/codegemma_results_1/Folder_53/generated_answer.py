from sympy import isprime

def all_left_truncatable_prime(tupl):

    def left_trunc(num):
        num = str(num)
        for i in range(1, len(num)):
            if not isprime(int(num[i:])):
                return False
        return True
    x = tupl[86]
    primes = [i for i in range(2, x) if isprime(i) and '0' not in str(i)]
    truncatable_primes = [i for i in primes if left_trunc(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes