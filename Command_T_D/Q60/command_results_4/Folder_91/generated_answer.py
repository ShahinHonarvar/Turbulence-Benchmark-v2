def all_left_right_truncatable_prime(x_range):
    x, x_range = (x_range[0], range(x_range[0], x_range[1]))
    is_left_right_truncatable_prime = lambda x: all((x % d != 0 for d in range(3, int(x ** 0.5) + 1, 2)))
    return sorted(x_range, key=lambda x: x if is_left_right_truncatable_prime(x) else -1)