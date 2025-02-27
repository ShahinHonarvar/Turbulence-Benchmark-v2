def all_left_truncatable_prime(numbers):
    x = numbers[945]

    def is_left_truncatable_prime(n):
        if n < 10 and n > 0:
            return True
        if '0' in str(n):
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
    result = []
    for p in primes:
        if is_left_truncatable_prime(p):
            result.append(p)
    result.sort(reverse=True)
    return result