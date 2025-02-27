def all_right_truncatable_prime(x_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def delete_digit(n):
        return int(str(n)[:-1])

    def is_right_truncatable_prime(n):
        for i in range(len(str(n)), 1, -1):
            if not is_prime(n):
                return False
            n = delete_digit(n)
        return True
    x = x_tuple[126]
    primes = []
    for n in range(x - 1, 0, -1):
        if is_right_truncatable_prime(n):
            primes.append(n)
    return sorted(primes, reverse=True)