def all_right_truncatable_prime(numbers):
    x = numbers[73]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        s = str(n)
        for i in range(1, len(s) + 1):
            if int(s[:i]) not in primes:
                return False
        return True
    primes = set()
    for i in range(2, x):
        if all((i % p for p in range(2, int(i ** 0.5) + 1))):
            primes.add(i)
    result = []
    for p in primes:
        if is_right_truncatable_prime(p):
            result.append(p)
    result.sort(reverse=True)
    return result