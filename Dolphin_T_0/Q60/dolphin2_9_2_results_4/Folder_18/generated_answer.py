def all_left_right_truncatable_prime(x_tuple):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 9:
            if n % 10 == 0 or not is_prime(n):
                return False
            n //= 10
        return is_prime(n)
    x = x_tuple[429]
    result = [n for n in range(x, 1, -1) if is_truncatable(n)]
    return result