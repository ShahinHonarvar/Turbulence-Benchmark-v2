def all_left_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(len(n_str) - 1, 0, -1):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    primes = []
    for i in range(x - 1, 1, -1):
        if is_left_truncatable_prime(i):
            primes.append(i)
    return primes