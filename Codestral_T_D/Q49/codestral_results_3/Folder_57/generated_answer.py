def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    for i in range(2, 81):
        fib.append(fib[i - 1] + fib[i - 2])
    fib_80 = fib[80]
    return decimal % fib_80 == 0