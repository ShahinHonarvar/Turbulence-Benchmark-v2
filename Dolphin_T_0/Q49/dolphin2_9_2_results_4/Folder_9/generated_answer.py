def if_decimal_is_divisible(binary_rep):
    decimal_num = int(binary_rep, 2)
    fib = [0, 1]
    while len(fib) < 68:
        fib.append(fib[-1] + fib[-2])
    return decimal_num % fib[67] == 0