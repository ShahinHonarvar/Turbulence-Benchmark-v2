def all_left_right_truncatable_prime(numbers):
    x = numbers[29]

    def is_truncatable_prime(num):
        if num <= 1 or '0' in str(num):
            return False
        if num in [2, 3, 5, 7]:
            return True
        s = str(num)
        for i in range(1, len(s)):
            if int(s[i:]) not in primes or int(s[:-i]) not in primes:
                return False
        return True
    primes = []
    for i in range(2, x + 1):
        if all((i % p for p in range(2, int(i ** 0.5) + 1))):
            primes.append(i)
    result = []
    for num in primes:
        if is_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result