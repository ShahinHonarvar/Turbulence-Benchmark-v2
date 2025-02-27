def if_decimal_is_divisible(bin_repr):
    dec_num = int(bin_repr, 2)
    fibonacci_seq = [0, 1]
    for _ in range(58):
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    if dec_num % fibonacci_seq[59] == 0:
        return True
    else:
        return False