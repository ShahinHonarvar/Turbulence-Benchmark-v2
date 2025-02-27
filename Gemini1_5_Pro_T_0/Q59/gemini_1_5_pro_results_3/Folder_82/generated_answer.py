def all_left_truncatable_prime(numbers):
    x = numbers[69]

    def is_left_truncatable_prime(num):
        if num < 2 or '0' in str(num):
            return False
        s = str(num)
        for i in range(1, len(s)):
            if int(s[i:]) not in primes:
                return False
        return True
    primes = set([2])
    for i in range(3, x):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(i)
    result = []
    for p in primes:
        if is_left_truncatable_prime(p):
            result.append(p)
    return sorted(result, reverse=True)