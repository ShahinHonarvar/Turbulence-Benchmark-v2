def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for _ in range(2, 129):
        fib.append(fib[-1] + fib[-2])
    decimal_value = int(binary_str, 2)
    return decimal_value % fib[128] == 0