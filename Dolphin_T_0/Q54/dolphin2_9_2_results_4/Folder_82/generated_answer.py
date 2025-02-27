def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = numbers[69]
    primes = []
    for n in reversed(range(2, x)):
        if is_prime(n):
            m = n
            while m != 0 and is_prime(m):
                m = m // 10
            if m == 0:
                primes.append(n)
    return sorted(primes, reverse=True)