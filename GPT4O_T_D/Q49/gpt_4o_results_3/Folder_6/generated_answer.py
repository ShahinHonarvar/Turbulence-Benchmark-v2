def if_decimal_is_divisible(binary_str):
    fib_185 = 0
    a, b = (0, 1)
    for _ in range(185):
        a, b = (b, a + b)
    fib_185 = a
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_185 == 0