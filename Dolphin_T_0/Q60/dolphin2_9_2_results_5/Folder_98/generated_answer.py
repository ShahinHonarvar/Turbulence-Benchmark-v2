def all_left_right_truncatable_prime(y):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        i = 1
        while i < len(str(n)):
            if not is_prime(int(str(n)[i:])):
                return False
            i += 1
        i = 1
        while i < len(str(n)):
            if not is_prime(int(str(n)[:-i])):
                return False
            i += 1
        return True
    x = y[8]
    return sorted([i for i in range(2, x + 1) if is_prime(i) and is_truncatable(i)], reverse=True)