def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_and_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        for i in range(2, len(str(n))):
            if n % 10 ** i == 0:
                return False
        n = str(n)
        for i in range(len(n) - 1):
            if not is_prime(int(n[i + 1:])):
                return False
            if not is_prime(int(n[:-i - 1])):
                return False
        return True
    result = []
    for i in range(x, 0, -1):
        if is_left_and_right_truncatable(i) and i <= x:
            result.append(i)
    return result