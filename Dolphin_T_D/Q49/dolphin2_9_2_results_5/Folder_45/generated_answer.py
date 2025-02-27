def if_decimal_is_divisible(bin_str):
    decimal_num = int(bin_str, 2)
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < 28:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    if decimal_num % fibonacci_seq[27] == 0:
        return True
    else:
        return False