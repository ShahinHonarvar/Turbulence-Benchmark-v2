def all_left_truncatable_prime(a_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def contain_zero(n):
        while n != 0:
            if n % 10 == 0:
                return True
            n = n // 10
        return False
    x = a_tuple[14]
    left_truncatable_primes = [i for i in range(x, 1, -1) if contain_zero(i) or not all((is_prime(i // 10 ** j) for j in range(1, len(str(i)) + 1)))]
    return sorted(left_truncatable_primes, reverse=True)