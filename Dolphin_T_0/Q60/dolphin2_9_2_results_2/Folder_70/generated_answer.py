def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 9:
            if is_prime(n):
                n = int(str(n)[1:-1])
            else:
                return False
        return is_prime(n)
    x = t[433]
    prime_list = [n for n in range(2, x + 1) if is_prime(n)]
    truncatable_list = [n for n in prime_list if is_truncatable(n)]
    return sorted(truncatable_list, reverse=True)