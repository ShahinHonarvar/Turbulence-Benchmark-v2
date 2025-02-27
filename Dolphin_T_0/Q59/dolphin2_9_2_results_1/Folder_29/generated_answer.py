def all_left_truncatable_prime(my_tuple):

    def is_left_truncatable(n):
        n = str(n)
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = my_tuple[55]
    left_truncatable_primes = []
    for i in range(x - 1, 0, -1):
        if is_left_truncatable(i):
            left_truncatable_primes.append(i)
    return left_truncatable_primes