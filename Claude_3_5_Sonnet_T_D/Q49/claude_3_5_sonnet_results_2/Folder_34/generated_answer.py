def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1]
    while len(fib) < 24:
        fib.append(fib[-1] + fib[-2])
    fibonacci_24th = fib[23]
    return decimal % fibonacci_24th == 0