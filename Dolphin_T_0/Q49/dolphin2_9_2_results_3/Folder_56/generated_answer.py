def if_decimal_is_divisible(binary):
    fib = [0, 1]
    for i in range(2, 84):
        fib.append(fib[i - 1] + fib[i - 2])
    arabic = int(binary, 2)
    return arabic % fib[83] == 0