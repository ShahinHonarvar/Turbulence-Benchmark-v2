def if_decimal_is_divisible(binary):
    dec = int(binary, 2)
    fib1 = 0
    fib2 = 1
    for i in range(75):
        fib1, fib2 = (fib2, fib1 + fib2)
    return dec % fib2 == 0