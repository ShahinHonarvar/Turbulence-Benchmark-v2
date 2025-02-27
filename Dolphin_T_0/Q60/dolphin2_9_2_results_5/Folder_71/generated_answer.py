def all_left_right_truncatable_prime(n):

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def is_truncatable(x):
        if not is_prime(int(x)):
            return False
        while x:
            if x % 10 == 0:
                return False
            x //= 10
        return True
    x = n[22]
    result = []
    for i in range(x, 100, -1):
        if is_truncatable(i):
            result.append(i)
    return result