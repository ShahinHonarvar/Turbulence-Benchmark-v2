def if_decimal_is_divisible(binary_str):
    fib_seq = [0]
    while len(fib_seq) <= 108:
        fib_seq.append(fib_seq[len(fib_seq) - 2] + fib_seq[len(fib_seq) - 1])
    decimal_num = int(binary_str, 2)
    for num in fib_seq:
        if decimal_num % num == 0:
            return True
    return False