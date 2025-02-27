def if_decimal_is_divisible(binary_str):
    fib1, fib2 = (0, 1)
    for _ in range(66):
        fib1, fib2 = (fib2, fib1 + fib2)
    num = int(binary_str, 2)
    return num % fib1 == 0