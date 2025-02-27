def all_left_truncatable_prime(tuple_int):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tuple_int[86]
    ret = [n for n in range(x, 1, -1) if all(is_prime(int(str(n).replace(str(n)[0], '')))) and all(is_prime(n)) and (not '0' in str(n))]
    return ret