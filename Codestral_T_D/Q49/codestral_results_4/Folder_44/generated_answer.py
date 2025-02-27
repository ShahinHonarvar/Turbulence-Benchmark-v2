def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1] + [0] * 157
    for i in range(2, 160):
        fib[i] = fib[i - 1] + fib[i - 2]
    return decimal % fib[159] == 0