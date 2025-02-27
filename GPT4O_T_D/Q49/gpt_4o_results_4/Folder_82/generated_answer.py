def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 100):
        fib.append(fib[i - 1] + fib[i - 2])
    fib_number = fib[99]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_number == 0