def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[54]
    truncable_primes = []
    for i in range(1, x):
        if is_prime(i):
            truncation = i
            while truncation:
                if not is_prime(truncation):
                    break
                truncation //= 10
            else:
                truncable_primes.append(i)
    return sorted(truncable_primes)