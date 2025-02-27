def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_137 = [0, 1]
    while len(fib_137) < 137:
        fib_137.append(fib_137[-1] + fib_137[-2])
    return decimal % fib_137[136] == 0