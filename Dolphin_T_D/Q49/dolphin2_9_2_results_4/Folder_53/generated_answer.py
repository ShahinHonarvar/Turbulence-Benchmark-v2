def if_decimal_is_divisible(binary):
    fib = [0, 1]
    for i in range(2, 65):
        fib.append(fib[-1] + fib[-2])
    if_divisible = fib[64]
    decimal = int(binary, 2)
    return decimal % if_divisible == 0