def if_decimal_is_divisible(binary_rep):
    decimal_num = int(binary_rep, 2)
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < 119:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    fibonacci_119th = fibonacci_seq[118]
    return decimal_num % fibonacci_119th == 0