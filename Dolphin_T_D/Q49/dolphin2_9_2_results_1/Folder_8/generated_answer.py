def if_decimal_is_divisible(binary):
    FIBONACCI_NUMBER = 54
    decimal = int(binary, 2)
    fib = [0, 1]
    current = fib[1]
    next = fib[0] + fib[1]
    while len(fib) < FIBONACCI_NUMBER:
        fib.append(next)
        current, next = (next, current + next)
    return decimal % fib[FIBONACCI_NUMBER - 1] == 0