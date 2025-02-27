from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(1, len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:i])):
                return False
        return True
    x = numbers[29]
    truncatable_primes = []
    for n in range(11, x + 1):
        if '0' not in str(n) and isprime(n) and is_truncatable_prime(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes)