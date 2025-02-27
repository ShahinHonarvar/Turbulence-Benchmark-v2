def if_decimal_is_divisible(binary_str):
    n = int(binary_str, 2)
    i = 0
    fib1 = 0
    fib2 = 1
    while i < 168:
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
        i += 1
    return n % fib == 0