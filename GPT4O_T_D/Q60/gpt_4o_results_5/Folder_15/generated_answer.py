from sympy import isprime

def all_left_right_truncatable_prime(t):

    def is_left_right_truncatable(n):
        s = str(n)
        while len(s) > 0:
            if not isprime(int(s)):
                return False
            s = s[1:-1]
        return True
    x = t[6]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_left_right_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)