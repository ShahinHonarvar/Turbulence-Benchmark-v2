def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1]
    for i in range(2, 67):
        fib.append(fib[i - 1] + fib[i - 2])
    return decimal % fib[66] == 0