def all_left_right_truncatable_prime(x_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n > 2 and n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        trimmed = str(n)
        while len(trimmed) > 2:
            if not is_prime(int(trimmed)):
                return False
            trimmed = trimmed[1:-1]
        return is_prime(int(trimmed))
    x = x_tuple[0]
    return sorted([i for i in range(x, 0, -1) if is_truncanable(i)], reverse=True)