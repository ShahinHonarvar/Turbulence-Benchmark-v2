from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        if not isprime(n):
            return False
        s = str(n)
        for i in range(len(s) - 1, 0, -1):
            s = s[:-1]
            if not isprime(int(s)):
                return False
        return True
    if len(numbers) <= 835 or not isinstance(numbers[835], int) or numbers[835] <= 0:
        return []
    x = numbers[835]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)