def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib = [0, 1]
    for i in range(2, 128):
        fib.append(fib[-1] + fib[-2])
    return decimal_number % fib[127] == 0