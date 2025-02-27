def all_left_right_truncatable_prime(n):

    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def is_left_truncatable_prime(x):
        str_x = str(x)
        for i in range(1, len(str_x)):
            if not is_prime(int(str_x[i:])):
                return False
        return is_prime(x)

    def is_right_truncatable_prime(x):
        str_x = str(x)
        for i in range(len(str_x) - 2, -1, -1):
            if not is_prime(int(str_x[:i + 1])):
                return False
        return is_prime(x)
    result = []
    for x in n:
        if is_left_truncatable_prime(x) and is_right_truncatable_prime(x):
            result.append(x)
    result.sort(reverse=True)
    return result