def all_left_right_truncatable_prime(tup):
    x = tup[79]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            left = int(str_n[i:])
            right = int(str_n[:-i])
            if not (is_prime(left) and is_prime(right)):
                return False
        return True
    result = []
    for i in range(x, 2, -1):
        if is_truncatable(i) and is_prime(i):
            result.append(i)
    return result or []