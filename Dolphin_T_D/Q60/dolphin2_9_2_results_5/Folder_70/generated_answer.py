def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while len(str_n) > 1:
            if not is_prime(int(str_n[1:])) or not is_prime(int(str_n[:-1])):
                return False
            str_n = str_n[1:]
            str_n = str_n[:-1]
        return True
    x = num_tuple[433]
    primes = [n for n in range(x, -1, -1) if is_truncatable_prime(n)]
    return primes