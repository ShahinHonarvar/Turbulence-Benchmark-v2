def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fib = [0, 1]
    while len(fib) < 35:
        fib.append(fib[-1] + fib[-2])
    return decimal_value % fib[34] == 0