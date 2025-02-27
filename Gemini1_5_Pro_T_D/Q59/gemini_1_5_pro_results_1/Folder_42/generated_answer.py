def all_left_truncatable_prime(numbers):
    x = numbers[64]

    def is_left_truncatable_prime(n):
        if n < 10 or '0' in str(n):
            return False
        s = str(n)
        for i in range(1, len(s)):
            if int(s[i:]) not in primes:
                return False
        return True
    primes = set()
    for i in range(2, x):
        if all((i % p for p in primes)):
            primes.add(i)
    left_truncatable_primes = []
    for p in primes:
        if is_left_truncatable_prime(p):
            left_truncatable_primes.append(p)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes