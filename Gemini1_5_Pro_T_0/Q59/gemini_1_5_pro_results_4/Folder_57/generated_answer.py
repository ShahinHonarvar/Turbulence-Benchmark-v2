def all_left_truncatable_prime(numbers):
    x = numbers[54]

    def is_left_truncatable_prime(n):
        if n < 10:
            return False
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if int(s[i:]) not in primes:
                return False
        return True
    primes = []
    for i in range(2, x):
        if all((i % j for j in range(2, int(i ** 0.5) + 1))):
            primes.append(i)
    left_truncatable_primes = []
    for p in primes:
        if is_left_truncatable_prime(p):
            left_truncatable_primes.append(p)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes