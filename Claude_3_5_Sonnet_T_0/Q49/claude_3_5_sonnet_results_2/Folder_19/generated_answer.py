def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1]
    while len(fib) < 29:
        fib.append(fib[-1] + fib[-2])
    divisor = fib[28]
    return decimal % divisor == 0