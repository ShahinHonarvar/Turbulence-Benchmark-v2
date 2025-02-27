def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 119):
        fib.append(fib[i - 1] + fib[i - 2])
    num = int(binary_str, 2)
    return num % fib[118] == 0