def all_left_right_truncatable_prime(n):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        while len(str(n)) > 1:
            if str(n)[0] == '0' or str(n)[-1] == '0' or (not is_prime(n)):
                return False
            n = n // 10 if str(n)[0] == str(n)[-1] else int(str(n)[1:-1])
        return is_prime(n)
    return sorted([n for n in range(n) if is_left_right_truncatable(n)])