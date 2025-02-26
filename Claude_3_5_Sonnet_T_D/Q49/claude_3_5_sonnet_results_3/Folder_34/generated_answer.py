def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_24 = [0, 1]
    for _ in range(22):
        fib_24.append(fib_24[-1] + fib_24[-2])
    return decimal % fib_24[-1] == 0