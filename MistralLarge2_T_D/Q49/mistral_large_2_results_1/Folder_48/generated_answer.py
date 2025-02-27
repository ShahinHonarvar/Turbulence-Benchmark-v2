def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib1, fib2 = (0, 1)
    for _ in range(198):
        fib1, fib2 = (fib2, fib1 + fib2)
    return decimal % fib2 == 0