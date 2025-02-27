def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_left(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if n_str[i] == '0':
                return False
            if is_prime(int(n_str[i:])):
                n_str = n_str[:-1]
            else:
                return False
        return is_prime(int(n_str))

    def is_truncatable_right(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if n_str[i] == '0':
                return False
            if is_prime(int(n_str[:-i - 1])):
                n_str = n_str[:-1]
            else:
                return False
        return is_prime(int(n_str))
    x = t[69]
    primes = []
    for i in range(2, x + 1):
        if is_truncatable_left(i) and is_truncatable_right(i):
            primes.append(i)
    return sorted(primes, reverse=True)