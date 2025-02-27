def if_decimal_is_divisible(binary_str):
    decimal_integer = int(binary_str, 2)
    fib = [0, 1]
    for i in range(2, 145):
        fib.append(fib[i - 1] + fib[i - 2])
    return decimal_integer % fib[144] == 0