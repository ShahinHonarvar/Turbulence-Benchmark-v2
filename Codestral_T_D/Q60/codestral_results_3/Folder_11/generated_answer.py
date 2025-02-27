def all_left_right_truncatable_prime(lst):

    def is_truncated_prime(n):
        if n < 2:
            return False
        for i in range(1, len(str(n))):
            if int(str(n)[i:]) not in primes or int(str(n)[:-i]) not in primes:
                return False
        return True
    primes = [i for i in range(2, max(lst) + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    x = lst[86]
    return sorted([i for i in primes if i <= x and is_truncated_prime(i)])