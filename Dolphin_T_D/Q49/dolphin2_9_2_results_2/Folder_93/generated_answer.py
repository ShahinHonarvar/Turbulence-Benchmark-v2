def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib59 = [0, 1]
    while len(fib59) < 59:
        fib59.append(fib59[-2] + fib59[-1])
        if fib59[-1] > decimal:
            break
    return decimal % fib59[-1] == 0