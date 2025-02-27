def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    fib_sequence = [0, 1]
    while len(str(fib_sequence[-1] + fib_sequence[-2])) < len(str(decimal_num)):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[113] != 0 and decimal_num % fib_sequence[113] == 0