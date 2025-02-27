def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[433]

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable(n):
        if n < 10:
            return is_prime(n)
        elif n % 10 == 0 or n // 10 % 10 == 0:
            return False
        else:
            return is_truncatable(n // 10) and is_prime(n % 10) and is_truncatable(n // 10)
    result = []
    for i in reversed(range(2, x + 1)):
        if is_prime(i) and is_truncatable(i):
            result.append(i)
    return result