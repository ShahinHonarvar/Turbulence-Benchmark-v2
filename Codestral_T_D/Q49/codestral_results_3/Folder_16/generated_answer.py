def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < 128:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return decimal_num % fibonacci_seq[128 - 1] == 0