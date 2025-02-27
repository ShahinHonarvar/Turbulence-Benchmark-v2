def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 4:
        fib_sequence.append(fib_sequence[-2] + fib_sequence[-1])
    fourth_fib_number = fib_sequence[3]
    return decimal_num % fourth_fib_number == 0