import sympy

def all_left_right_truncatable_prime(numbers):

    def is_truncatable(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        while len(str_n) > 1:
            str_n = str_n[1:-1]
            if str_n and (not sympy.isprime(int(str_n))):
                return False
        return True
    x = numbers[86]
    primes = list(sympy.primerange(2, x + 1))
    result = [p for p in primes if is_truncatable(p)]
    return result