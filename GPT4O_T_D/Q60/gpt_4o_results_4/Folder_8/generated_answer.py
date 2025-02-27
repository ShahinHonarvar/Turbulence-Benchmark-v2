from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(1, len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:i])):
                return False
        return True
    x = numbers[41]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        if isprime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)