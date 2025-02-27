def if_decimal_is_divisible(binary_str):
    fib1, fib2 = (0, 1)
    for _ in range(38):
        fib1, fib2 = (fib2, fib1 + fib2)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib2 == 0