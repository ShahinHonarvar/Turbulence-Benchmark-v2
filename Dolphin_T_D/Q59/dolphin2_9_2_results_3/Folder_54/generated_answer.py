def all_left_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        str_n = str(n)
        while len(str_n) != 0:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable(n)], reverse=True)