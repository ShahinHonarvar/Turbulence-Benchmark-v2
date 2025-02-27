def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib = [0, 1]
    while len(fib) < 175:
        fib.append(fib[-1] + fib[-2])
    fib_174 = fib[-1]
    return decimal % fib_174 == 0