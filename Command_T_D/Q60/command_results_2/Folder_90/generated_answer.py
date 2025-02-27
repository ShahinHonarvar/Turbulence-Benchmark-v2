def all_left_right_truncatable_prime(x_value):
    return [int(i) for i in range(2, x_value[0] + 1) if all((str(i).count(d) == 1 for d in str(i)))]