def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib = [0, 1]
    for i in range(2, 119):
        fib.append(fib[i - 1] + fib[i - 2])
    return decimal % fib[-1] == 0