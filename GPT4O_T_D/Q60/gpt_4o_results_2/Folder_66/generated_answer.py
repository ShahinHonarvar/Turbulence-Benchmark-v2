from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:len(s) - i])):
                return False
        return True
    x = numbers[25]
    truncatable_primes = [n for n in range(10, x + 1) if isprime(n) and '0' not in str(n) and is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)