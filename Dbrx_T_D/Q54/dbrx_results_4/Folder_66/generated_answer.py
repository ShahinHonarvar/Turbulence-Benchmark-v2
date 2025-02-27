from sympy import isprime

def all_right_truncatable_prime(x: int) -> list[int]:

    def is_right_truncatable(n: int) -> bool:
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True
    primes = [i for i in range(2, x) if is_right_truncatable(i)]
    primes.sort(reverse=True)
    return primes