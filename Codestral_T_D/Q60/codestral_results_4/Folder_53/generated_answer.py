def all_left_right_truncatable_prime(t):

    def is_trunc_prime(n):
        if n < 2:
            return False
        for i in range(1, len(str(n))):
            if int(str(n)[i:]) not in primes or int(str(n)[:i]) not in primes:
                return False
        return True
    primes = [i for i in range(2, t[86] + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    return sorted([i for i in primes if is_trunc_prime(i) and '0' not in str(i)], reverse=True)