def if_decimal_is_divisible(binary_string):
    fib1, fib2 = (0, 1)
    for _ in range(28):
        fib1, fib2 = (fib2, fib1 + fib2)
    decimal_value = int(binary_string, 2)
    return decimal_value % fib1 == 0