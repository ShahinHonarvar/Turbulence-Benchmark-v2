def all_right_truncatable_prime(tup_of_positive_integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        else:
            return is_prime(n) and is_right_truncatable(n // 10)
    right_truncatable_primes = []
    x = tup_of_positive_integers[22]
    for i in range(x - 1, 1, -1):
        if is_right_truncatable(i) and is_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True) if right_truncatable_primes else []