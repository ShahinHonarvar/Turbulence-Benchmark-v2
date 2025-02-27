def if_decimal_is_divisible(binary_string):
    fib_seq = [0, 1]
    for _ in range(2, 109):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    num = int(binary_string, 2)
    return num % fib_seq[108] == 0