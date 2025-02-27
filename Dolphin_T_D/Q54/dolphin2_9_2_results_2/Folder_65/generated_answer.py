def all_right_truncatable_prime(primes_tuple):
    x = primes_tuple[32]
    rst = list()

    def is_prime(n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return False
            else:
                return True
        else:
            return False

    def is_right_truncatable_prime(n):
        if is_prime(n):
            for i in range(1, len(str(n))):
                if not is_prime(int(n / 10 ** i)):
                    return False
        else:
            return False
        return True
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            rst.append(i)
    return sorted(rst)