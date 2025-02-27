def if_decimal_is_divisible(binary_str):
    fib_n = [0, 1]
    for _ in range(113):
        fib_n.append(fib_n[-1] + fib_n[-2])
    decimal = int(binary_str, 2)
    return decimal % fib_n[114] == 0