def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    primes = [True] * (x + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, x + 1, i):
                primes[j] = False

    def truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not primes[int(s[i:])] or not primes[int(s[:-i or None])]:
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if primes[i] and truncatable_prime(i):
            result.append(i)
    return result