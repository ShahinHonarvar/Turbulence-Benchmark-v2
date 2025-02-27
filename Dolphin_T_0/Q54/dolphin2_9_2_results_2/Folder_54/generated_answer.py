def all_right_truncatable_prime(x_tuple):
    x = x_tuple[88]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        if not is_prime(num):
            return False
        while len(str(num)) > 1:
            num = int(str(num)[:-1])
            if not is_prime(num):
                return False
        return True
    primes = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    return sorted(primes, reverse=True)