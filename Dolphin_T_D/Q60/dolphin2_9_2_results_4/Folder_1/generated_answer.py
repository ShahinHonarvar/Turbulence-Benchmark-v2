def all_left_right_truncatable_prime(int_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 2:
            return False
        for digit in str(n):
            if digit == '0':
                return False
        while len(str(n)) > 1:
            if not is_prime(n):
                return False
            n = n // 10
            n = n % pow(10, len(str(n)))
        return is_prime(int(str(n)[-1]))
    x = int_tuple[20]
    result = []
    for n in range(x, 1, -1):
        if is_truncatable(n):
            result.append(n)
    return sorted(result, reverse=True)