def all_left_truncatable_prime(numbers):
    x = numbers[49]
    primes = [True] * x
    primes[0] = primes[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, x, i):
                primes[j] = False

    def is_left_truncatable(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not primes[int(str_n[i:])]:
                return False
        return True
    left_truncatable_primes = [n for n in range(2, x) if str(n)[0] != '0' and is_left_truncatable(n)]
    return sorted(left_truncatable_primes)