def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 34):
        fib.append(fib[i - 1] + fib[i - 2])
    decimal = int(binary_str, 2)
    return decimal in [i for i in fib if i % 34 == 0]