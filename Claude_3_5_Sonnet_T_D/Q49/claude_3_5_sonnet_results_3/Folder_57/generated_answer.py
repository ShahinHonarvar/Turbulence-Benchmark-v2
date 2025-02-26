def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fib_prev, fib_curr = (0, 1)
    for _ in range(79):
        fib_prev, fib_curr = (fib_curr, fib_prev + fib_curr)
    return decimal_num % fib_curr == 0