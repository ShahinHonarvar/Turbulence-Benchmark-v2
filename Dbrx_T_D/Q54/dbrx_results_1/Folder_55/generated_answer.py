def all_right_truncatable_prime(n_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        while num > 0:
            if not is_prime(num):
                return False
            num = int(str(num)[:-1])
        return True
    x = n_tuple[73]
    primes = []
    for num in range(1, x):
        if is_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)