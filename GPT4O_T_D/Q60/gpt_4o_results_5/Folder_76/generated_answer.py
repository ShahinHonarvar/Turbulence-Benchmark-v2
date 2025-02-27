from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not (isprime(int(s[i:])) and isprime(int(s[:i]))):
                return False
        return isprime(n)
    x = numbers[370]
    truncatable_primes = [n for n in range(10, x + 1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)