def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    for i in range(2, 129):
        fib.append(fib[i - 1] + fib[i - 2])
    decimal_number = int(binary_string, 2)
    return decimal_number % fib[128] == 0