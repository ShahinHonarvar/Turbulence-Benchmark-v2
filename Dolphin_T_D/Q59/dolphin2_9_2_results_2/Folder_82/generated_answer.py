def all_left_truncatable_prime(integer_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = integer_tuple[69]
    left_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i) and i % 10 != 0:
            j = i
            while j != 0:
                if not is_prime(j):
                    break
                j //= 10
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)