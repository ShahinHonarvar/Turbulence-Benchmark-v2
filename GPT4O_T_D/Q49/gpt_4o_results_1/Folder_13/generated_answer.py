def if_decimal_is_divisible(binary_str):
    fib_num = 0
    a, b = (0, 1)
    for _ in range(174):
        a, b = (b, a + b)
    fib_num = a
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_num == 0