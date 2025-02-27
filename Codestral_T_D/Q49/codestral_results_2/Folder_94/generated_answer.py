def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib = [0, 1]
    while len(fib) < 40:
        fib.append(fib[-1] + fib[-2])
    fib_40 = fib[-1]
    return decimal % fib_40 == 0