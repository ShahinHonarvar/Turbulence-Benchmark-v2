def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1]
    while len(fib) < 20:
        fib.append(fib[-1] + fib[-2])
    twentieth_fib = fib[19]
    return decimal % twentieth_fib == 0