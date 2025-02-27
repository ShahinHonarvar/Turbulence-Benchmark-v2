def all_right_truncatable_prime(tuple_):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tuple_[55]
    right_truncatable_primes = []
    for i in range(x, 0, -1):
        if is_prime(i):
            truncated = i
            while truncated > 0:
                if not is_prime(truncated):
                    break
                truncated = int(str(truncated)[:-1])
                if truncated == 0:
                    right_truncatable_primes.append(i)
                    break
    return sorted(right_truncatable_primes, reverse=True)