def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib = [0, 1]
    for _ in range(2, 111):
        fib.append(fib[-1] + fib[-2])
    return decimal_number % fib[110] == 0