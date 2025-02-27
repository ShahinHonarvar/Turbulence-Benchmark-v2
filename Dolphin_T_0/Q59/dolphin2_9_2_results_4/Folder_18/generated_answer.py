def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

    def is_left_truncatable(n):
        if n < 10:
            return True
        else:
            return is_prime(n // 10) and n % 10 != 0 and is_left_truncatable(n // 10)
    x = tup[429]
    result = []
    for i in range(x - 1, 1, -1):
        if is_left_truncatable(i) and is_prime(i):
            result.append(i)
    return result