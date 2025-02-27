def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if str(n)[-1] == '0':
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:-i])):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if is_prime(i) and is_truncatable(i)])