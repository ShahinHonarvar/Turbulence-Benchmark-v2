def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)
    fib1, fib2 = (0, 1)
    for _ in range(62):
        fib1, fib2 = (fib2, fib1 + fib2)
    return decimal % fib2 == 0