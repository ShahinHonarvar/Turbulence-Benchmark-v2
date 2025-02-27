def all_left_right_truncatable_prime(args):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_trim_prime(n):
        while len(str(n)) > 1:
            n = n % 10 ** (len(str(n)) - 1) + n // 10 ** (len(str(n)) - 1) * 10 ** (len(str(n)) - 2)
            if not is_prime(n):
                return False
        return True
    x = args[73]
    primes = [i for i in range(x, 1, -1) if is_prime(i) and is_trim_prime(i)]
    return primes