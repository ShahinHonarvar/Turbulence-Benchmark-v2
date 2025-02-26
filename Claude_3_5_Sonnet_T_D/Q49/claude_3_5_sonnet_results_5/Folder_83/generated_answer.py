def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_60 = [0, 1]
    for _ in range(58):
        fib_60.append(fib_60[-1] + fib_60[-2])
    return decimal % fib_60[-1] == 0