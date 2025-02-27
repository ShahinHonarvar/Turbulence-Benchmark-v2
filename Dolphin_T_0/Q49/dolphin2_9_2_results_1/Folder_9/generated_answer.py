def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib1 = 0
    fib2 = 1
    for i in range(67):
        fib1, fib2 = (fib2, fib1 + fib2)
    return decimal % fib2 == 0