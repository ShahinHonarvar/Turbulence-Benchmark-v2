def if_decimal_is_divisible(bin_string):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 47:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_47 = fib_sequence[46]
    decimal_num = int(bin_string, 2)
    return decimal_num % fib_47 == 0