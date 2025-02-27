def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_seq = [0, 1]
    for _ in range(2, 39):
        fib_seq.append(fib_seq[-2] + fib_seq[-1])
    return decimal % fib_seq[-1] == 0