def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1]
    for _ in range(173):
        fib.append(fib[-1] + fib[-2])
    divisor = fib[174]
    return decimal % divisor == 0