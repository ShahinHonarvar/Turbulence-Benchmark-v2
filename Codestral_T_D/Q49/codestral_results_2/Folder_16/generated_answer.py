def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1] + [0] * 127
    for i in range(2, 129):
        fib[i] = fib[i - 1] + fib[i - 2]
    return decimal % fib[128] == 0