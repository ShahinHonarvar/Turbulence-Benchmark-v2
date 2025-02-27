def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib = [0, 1]
    for i in range(2, 199 + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return decimal_number % fib[199] == 0