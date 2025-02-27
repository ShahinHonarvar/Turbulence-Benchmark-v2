def all_left_truncatable_prime(numbers):
    x = numbers[52]

    def is_left_truncatable_prime(num):
        if num < 10:
            return num > 1
        if '0' in str(num):
            return False
        s = str(num)
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