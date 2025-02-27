def all_left_truncatable_prime(tup):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        while num:
            if not is_prime(num):
                return False
            num = num // 10
        return True
    x = tup[1]
    left_truncatable_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    return sorted(left_truncatable_primes, reverse=True)