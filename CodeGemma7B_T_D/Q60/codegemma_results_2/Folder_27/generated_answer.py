def all_left_right_truncatable_prime(x):

    def is_prime(x):
        return x > 1 and all((x % y != 0 for y in range(2, int(x ** 0.5) + 1)))

    def is_truncatable(x):
        str_x = str(x)
        return all((is_prime(int(str_x[i:])) and is_prime(int(str_x[:-i])) for i in range(1, len(str_x))))
    result = []
    for i in range(2, x + 1):
        if str(i).count('0') == 0 and is_prime(i) and is_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)