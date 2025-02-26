def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_prev, fib_curr = (0, 1)
    for _ in range(176):
        fib_prev, fib_curr = (fib_curr, fib_prev + fib_curr)
    return decimal % fib_curr == 0