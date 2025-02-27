def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fib = [0, 1]
    for _ in range(2, 69):
        fib.append(fib[-1] + fib[-2])
    return decimal_number % fib[68] == 0