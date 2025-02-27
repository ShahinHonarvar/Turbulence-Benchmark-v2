def all_left_right_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        return all((is_prime(int(str_n[i:])) for i in range(len(str_n))))

    def is_right_truncatable_prime(n):
        str_n = str(n)
        return all((is_prime(int(str_n[:i])) for i in range(1, len(str_n))))
    x = tup[30]
    lst = [n for n in range(2, x + 1) if '0' not in str(n) and is_left_truncatable_prime(n) and is_right_truncatable_prime(n)]
    return sorted(lst)