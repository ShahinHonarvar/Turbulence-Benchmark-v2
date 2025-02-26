def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    while len(fib) < 48:
        fib.append(fib[-1] + fib[-2])
    divisor = fib[47]
    return decimal % divisor == 0