def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    while len(fib) < 189:
        fib.append(fib[-1] + fib[-2])
    fib_188 = fib[-1]
    decimal = int(binary_string, 2)
    return decimal % fib_188 == 0