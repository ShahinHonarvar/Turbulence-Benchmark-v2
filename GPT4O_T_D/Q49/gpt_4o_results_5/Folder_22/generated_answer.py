def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 21):
        fib.append(fib[i - 1] + fib[i - 2])
    fib_20th = fib[20]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_20th == 0