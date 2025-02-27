def all_left_right_truncatable_prime(x_tuple):
    x = int(x_tuple[57])

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n == 0:
            return False
        num = str(n)
        for i in range(1, len(num)):
            if not is_prime(int(num[i:]) or int(num[:i])):
                return False
        return True
    left_right_truncatables = []
    for n in range(x, 1, -1):
        if is_truncatable_prime(n):
            left_right_truncatables.append(n)
    return left_right_truncatables