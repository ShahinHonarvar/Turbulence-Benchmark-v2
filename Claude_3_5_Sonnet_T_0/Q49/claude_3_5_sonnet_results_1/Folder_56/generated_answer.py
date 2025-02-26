def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1]
    while len(fib) < 84:
        fib.append(fib[-1] + fib[-2])
    divisor = fib[83]
    return decimal % divisor == 0