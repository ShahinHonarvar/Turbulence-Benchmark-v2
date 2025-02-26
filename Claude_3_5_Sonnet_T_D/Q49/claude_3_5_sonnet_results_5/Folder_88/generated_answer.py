def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_prev, fib_current = (0, 1)
    for _ in range(48):
        fib_prev, fib_current = (fib_current, fib_prev + fib_current)
    return decimal % fib_current == 0