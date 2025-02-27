def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    for i in range(2, 110):
        fib.append(fib[i - 1] + fib[i - 2])
    return decimal % fib[109] == 0