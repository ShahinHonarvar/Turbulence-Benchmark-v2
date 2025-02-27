def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    a, b = (0, 1)
    for _ in range(54):
        a, b = (b, a + b)
    fib_54 = a
    return decimal % fib_54 == 0