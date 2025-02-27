def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        return str(n).count('0') == 0 and all((is_prime(int(str(n).replace(n % 10 * 10 ** len(str(n)) - n, ''))) for n in range(10 ** len(str(n)) // 10, 10 ** len(str(n)), 10)))
    result = []
    for i in range(2, x + 1):
        if is_truncatable(i) and is_prime(i):
            result.append(i)
    return result