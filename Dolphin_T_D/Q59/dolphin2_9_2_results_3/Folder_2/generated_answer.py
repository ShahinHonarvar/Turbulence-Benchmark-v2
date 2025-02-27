def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        n_list = [n]
        while n_list[-1] > 10:
            n_list.append(int(n_list[-1] * 0.1))
        return all(map(is_prime, n_list))
    x = t[618]
    primes = [n for n in range(2, x) if is_prime(n) and is_left_truncatable_prime(n)]
    return sorted(primes)