def if_decimal_is_divisible(binary_string):
    num_in_binary = int(binary_string, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 187:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return num_in_binary % fib_seq[186] == 0