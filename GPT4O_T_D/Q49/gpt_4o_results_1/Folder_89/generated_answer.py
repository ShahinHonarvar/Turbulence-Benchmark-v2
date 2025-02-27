def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 126):
        fib.append(fib[i - 1] + fib[i - 2])
    decimal_number = int(binary_str, 2)
    return decimal_number % fib[125] == 0