def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 136):
        fib.append(fib[-1] + fib[-2])
    fib_134 = fib[134]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_134 == 0