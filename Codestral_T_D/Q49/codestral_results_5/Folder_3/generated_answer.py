def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 35:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_num = fib_seq[34]
    return decimal_number % fib_num == 0