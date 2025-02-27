def all_left_right_truncatable_prime(int_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        while len(str(n)) > 1:
            n = int(str(n)[1:-1])
            if not is_prime(n):
                return False
        return True
    x = int_tuple[67]
    primes = []
    for i in range(x, 1, -1):
        if is_left_right_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)