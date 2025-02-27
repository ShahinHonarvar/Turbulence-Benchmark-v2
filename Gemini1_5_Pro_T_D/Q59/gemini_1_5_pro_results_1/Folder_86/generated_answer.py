def all_left_truncatable_prime(numbers):
    x = numbers[126]

    def is_left_truncatable_prime(n):
        if n < 10 or '0' in str(n):
            return False
        s = str(n)
        while len(s) > 1:
            s = s[1:]
            if not all((int(s) % i for i in range(2, int(s ** 0.5) + 1))):
                return False
        return all((n % i for i in range(2, int(n ** 0.5) + 1)))
    primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            primes.append(i)
    primes.sort(reverse=True)
    return primes