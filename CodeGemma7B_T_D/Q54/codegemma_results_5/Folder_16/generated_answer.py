def all_right_truncatable_prime(t):
    x = t[792]

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def is_right_truncatable_prime(x):
        for i in range(1, len(str(x))):
            if not is_prime(int(str(x)[:-i])):
                return False
        return True
    result = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)