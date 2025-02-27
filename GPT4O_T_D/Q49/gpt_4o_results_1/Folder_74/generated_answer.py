def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    for i in range(2, 167):
        fib.append(fib[-1] + fib[-2])
    number = int(binary_string, 2)
    return number % fib[166] == 0