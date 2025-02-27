def all_right_truncatable_prime(tuple_):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n) - 1, 0, -1):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    x = tuple_[1]
    return sorted([n for n in reversed(range(2, x)) if is_truncatable_prime(n)], reverse=False)