def if_decimal_is_divisible(bin_repr_decimal):
    decimal_num = int(bin_repr_decimal, 2)
    fibonacci_num = get_n_fibonacci_number(139)
    if decimal_num % fibonacci_num == 0:
        return True
    else:
        return False

def get_n_fibonacci_number(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(n - 2):
            a, b = (b, a + b)
        return b