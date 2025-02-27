def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for i in range(2, 59):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_sequence[58] == 0