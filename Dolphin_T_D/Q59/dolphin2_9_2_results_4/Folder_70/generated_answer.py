def all_left_truncatable_prime(num_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        if num < 10:
            return True
        elif num % 10 == 0:
            return False
        if not is_prime(num):
            return False
        return is_truncatable_prime(num // 10)
    x = num_tuple[433]
    left_truncatable_primes = [i for i in range(10, x - 1, -1) if is_prime(i) and is_truncatable_prime(i)]
    return left_truncatable_primes