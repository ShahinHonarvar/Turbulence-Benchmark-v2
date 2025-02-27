def if_decimal_is_divisible(binary_str):
    fib1, fib2 = (0, 1)
    for _ in range(179):
        fib1, fib2 = (fib2, fib1 + fib2)
    decimal_number = int(binary_str, 2)
    return decimal_number % fib1 == 0