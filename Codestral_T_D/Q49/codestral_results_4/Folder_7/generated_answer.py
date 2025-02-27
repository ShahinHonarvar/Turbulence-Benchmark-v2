def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib = [0, 1]
    while len(fib) < 160:
        fib.append(fib[-1] + fib[-2])
    return decimal % fib[159] == 0