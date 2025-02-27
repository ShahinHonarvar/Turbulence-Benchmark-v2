def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib = [0, 1]
    for _ in range(2, 95):
        fib.append(fib[-1] + fib[-2])
    return decimal_num % fib[94] == 0