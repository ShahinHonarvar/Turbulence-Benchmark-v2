def all_right_truncatable_prime(numbers):
    x = numbers[49]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j > 1:
                if is_prime(j):
                    j //= 10
                else:
                    break
            if j == 1:
                primes.append(i)
    return sorted(primes)