from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not (s and isprime(int(s))):
                return False
        return True
    if len(numbers) < 89:
        return []
    x = numbers[88]
    left_right_truncatable_primes = [n for n in range(2, x + 1) if isprime(n) and is_truncatable_prime(n)]
    return sorted(left_right_truncatable_primes, reverse=True)