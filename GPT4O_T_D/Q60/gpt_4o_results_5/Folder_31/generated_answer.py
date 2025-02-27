import sympy

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable_prime(n):
        s = str(n)
        while len(s) > 0 and sympy.isprime(int(s)):
            s = s[1:-1]
        return len(s) == 0
    number_x = numbers[50]
    truncatable_primes = []
    for i in range(2, number_x + 1):
        if '0' not in str(i) and sympy.isprime(i) and is_left_right_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)