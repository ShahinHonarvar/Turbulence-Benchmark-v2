def if_decimal_is_divisible(binary_repr_decimal):
    dec = int(binary_repr_decimal, 2)
    fib = [0, 1]
    while len(fib) < 38:
        fib.append(fib[-1] + fib[-2])
    return dec % fib[37] == 0