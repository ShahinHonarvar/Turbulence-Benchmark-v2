def if_decimal_is_divisible(binary_string):
    fib_seq = [0, 1]
    for _ in range(2, 165):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    number_dec = int(binary_string, 2)
    return number_dec % fib_seq[164] == 0