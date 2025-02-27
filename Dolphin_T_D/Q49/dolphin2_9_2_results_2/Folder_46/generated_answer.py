def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib1 = fib2 = 1
    for _ in range(138):
        decimal, fib1, fib2 = (fib2, fib2 + fib1, fib1)
    return decimal % fib1 == 0