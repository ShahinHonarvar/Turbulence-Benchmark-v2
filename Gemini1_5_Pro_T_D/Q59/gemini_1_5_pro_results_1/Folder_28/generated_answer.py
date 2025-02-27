def all_left_truncatable_prime(numbers):
    x = numbers[19]

    def is_left_truncatable_prime(n):
        if n < 10 and n in (2, 3, 5, 7):
            return True
        if '0' in str(n) or n < 2:
            return False
        s = str(n)
        for i in range(1, len(s)):
            if int(s[i:]) not in primes:
                return False
        return True
    primes = set()
    for num in range(2, x):
        if all((num % i for i in range(2, int(num ** 0.5) + 1))):
            primes.add(num)
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)