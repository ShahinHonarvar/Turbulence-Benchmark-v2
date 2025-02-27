def all_left_truncatable_prime(numbers):
    x = numbers[69]

    def is_left_truncatable_prime(n):
        if n < 2 or '0' in str(n):
            return False
        s = str(n)
        for i in range(1, len(s)):
            if int(s[i:]) not in primes:
                return False
        return True
    primes = {2}
    for i in range(3, x, 2):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
            if p * p > i:
                break
        if is_prime:
            primes.add(i)
    result = []
    for p in primes:
        if is_left_truncatable_prime(p):
            result.append(p)
    result.sort(reverse=True)
    return result