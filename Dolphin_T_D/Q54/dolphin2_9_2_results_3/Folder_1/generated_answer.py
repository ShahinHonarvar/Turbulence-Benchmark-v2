def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if is_prime(n):
            last_digit = n % 10
            n //= 10
            return n != 0 and is_right_truncatable_prime(n)
        return False
    x = num_tuple[20]
    primes = []
    for i in range(x, 1, -1):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)