def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    for i in range(2, 187):
        fib.append(fib[-1] + fib[-2])
    decimal_integer = int(binary_string, 2)
    return decimal_integer % fib[186] == 0