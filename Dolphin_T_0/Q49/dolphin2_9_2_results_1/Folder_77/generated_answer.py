def if_decimal_is_divisible(binary_string):
    num_fibonacci = 110
    fib_sequence = [0, 1]
    while len(fib_sequence) <= num_fibonacci:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal_num = int(binary_string, 2)
    return decimal_num % fib_sequence[num_fibonacci - 1] == 0