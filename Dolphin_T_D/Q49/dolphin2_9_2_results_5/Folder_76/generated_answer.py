def if_decimal_is_divisible(binary):
    dec = int(binary, 2)
    fib = [0, 1]
    for i in range(2, 189):
        fib.append(fib[i - 1] + fib[i - 2])
    return dec % fib[-1] == 0