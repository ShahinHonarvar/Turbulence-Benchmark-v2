def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib = [0, 1]
    while len(fib) < 54:
        fib.append(fib[-1] + fib[-2])
    fib_54 = fib[-1]
    return decimal % fib_54 == 0