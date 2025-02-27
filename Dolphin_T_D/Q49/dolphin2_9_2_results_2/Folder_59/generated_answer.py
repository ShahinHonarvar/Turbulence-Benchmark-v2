def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    i = 66
    fib1 = 1896952
    fib2 = 2036545
    while i < 74:
        fib1, fib2 = (fib2, fib1 + fib2)
        i += 1
    if decimal % fib2 == 0:
        return True
    else:
        return False