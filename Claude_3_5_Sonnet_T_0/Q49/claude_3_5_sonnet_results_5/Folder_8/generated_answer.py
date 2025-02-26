def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1]
    for _ in range(52):
        fib.append(fib[-1] + fib[-2])
    return decimal % fib[53] == 0