def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib = [0, 1]
    while len(fib) < 48:
        fib.append(fib[-1] + fib[-2])
    return decimal % fib[47] == 0