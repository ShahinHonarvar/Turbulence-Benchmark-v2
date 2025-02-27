def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    for i in range(2, 189):
        fib.append(fib[-1] + fib[-2])
    fib_188 = fib[188]
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_188 == 0