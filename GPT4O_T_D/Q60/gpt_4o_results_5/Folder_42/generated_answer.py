from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        length = len(s)
        for i in range(length):
            if not isprime(int(s[i:])) or not isprime(int(s[:length - i])):
                return False
        return True
    x = numbers[64]
    primes = [n for n in range(2, x + 1) if isprime(n)]
    result = [prime for prime in primes if is_truncatable_prime(prime)]
    result.sort(reverse=True)
    return result