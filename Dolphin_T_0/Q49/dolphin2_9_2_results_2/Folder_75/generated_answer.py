def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib = [0, 1]
    while len(bin(fib[-1])) < len(binary):
        fib.append(fib[-1] + fib[-2])
    return decimal % fib[-1] == 0