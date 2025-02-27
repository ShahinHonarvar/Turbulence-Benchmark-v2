def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_189 = 0
    fib_1 = 0
    fib_2 = 1
    for _ in range(189):
        fib_189 = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_189
    if decimal % fib_189 == 0:
        return True
    else:
        return False