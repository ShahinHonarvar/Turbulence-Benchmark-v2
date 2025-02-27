def all_left_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        n_string = str(n)
        for i in range(len(n_string) - 1, 0, -1):
            if n_string[i] == '0':
                return False
            if not is_prime(int(n_string[i:])):
                return False
        return True
    primes = [n for n in range(2, x) if is_prime(n)]
    return [n for n in primes if is_left_truncatable_prime(n)]