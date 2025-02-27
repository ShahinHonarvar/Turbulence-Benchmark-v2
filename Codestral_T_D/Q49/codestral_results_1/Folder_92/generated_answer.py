def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_num = 0
    a, b = (0, 1)
    for _ in range(7):
        fib_num = a
        a, b = (b, a + b)
    return decimal % fib_num == 0