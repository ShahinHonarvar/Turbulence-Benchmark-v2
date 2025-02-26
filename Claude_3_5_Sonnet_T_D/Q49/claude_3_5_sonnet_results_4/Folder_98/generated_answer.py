def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1]
    while len(fib) < 14:
        fib.append(fib[-1] + fib[-2])
    return decimal % fib[13] == 0