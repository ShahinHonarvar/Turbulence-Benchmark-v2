from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        if not isprime(n):
            return False
        length = len(s)
        for i in range(1, length):
            if not isprime(int(s[i:])) or not isprime(int(s[:i])):
                return False
        return True
    x = numbers[760]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)