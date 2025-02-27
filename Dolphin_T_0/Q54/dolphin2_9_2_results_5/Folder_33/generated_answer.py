def all_right_truncatable_prime(x_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = x_tuple[945]
    right_truncatable_primes = list()
    for num in range(x - 1, 0, -1):
        if is_prime(num) and all(is_prime((int(str(num)[:-i]) for i in range(1, len(str(num)))))):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)