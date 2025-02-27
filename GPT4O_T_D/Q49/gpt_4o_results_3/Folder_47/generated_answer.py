def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 95):
        fib.append(fib[i - 1] + fib[i - 2])
    fib_94th = fib[94]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_94th == 0