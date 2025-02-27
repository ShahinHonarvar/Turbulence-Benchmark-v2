def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib1, fib2 = (0, 1)
    for _ in range(195):
        fib1, fib2 = (fib2, fib1 + fib2)
    return decimal % fib1 == 0