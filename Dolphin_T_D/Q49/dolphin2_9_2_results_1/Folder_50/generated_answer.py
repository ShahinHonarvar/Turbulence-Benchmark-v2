def if_decimal_is_divisible(binary_rep):
    fib = [0, 1]
    while len(fib) < 120:
        fib.append(fib[-2] + fib[-1])
    target_num = 119
    decimal_num = int(binary_rep, 2)
    return decimal_num % fib[target_num] == 0