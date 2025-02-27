def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_trunc(n):
        if n <= 0:
            return False
        if n // 10 <= 0:
            return True
        return left_trunc(n // 10) and is_prime(n // 10)
    x = t[630]
    result = []
    for n in range(x - 1, 0, -1):
        if left_trunc(n) and is_prime(n):
            result.append(n)
    return result