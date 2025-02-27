def all_right_truncatable_prime(tuple_of_positive_integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 2:
            return False
        s = str(n)
        for i in range(len(s) - 1, 0, -1):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = tuple_of_positive_integers[32]
    return sorted([n for n in range(x) if is_right_truncatable(n) and is_prime(n)])