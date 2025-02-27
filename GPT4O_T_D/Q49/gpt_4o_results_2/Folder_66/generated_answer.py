def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 121):
        fib.append(fib[-1] + fib[-2])
    number = int(binary_str, 2)
    return number % fib[120] == 0