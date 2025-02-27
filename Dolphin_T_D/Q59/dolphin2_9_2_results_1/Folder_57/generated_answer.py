def all_left_truncatable_prime(tup_int):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    def remove_left_digits(n):
        while n >= 10 and n % 10 != 0:
            n = n // 10
        return n
    x = tup_int[54]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = []
    for prime in primes:
        truncated = remove_left_digits(prime)
        while truncated != 0 and is_prime(truncated):
            truncated = remove_left_digits(truncated)
            if truncated != 0:
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)