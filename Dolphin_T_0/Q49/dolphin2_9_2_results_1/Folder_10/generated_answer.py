def if_decimal_is_divisible(binary_representation):
    decimal_num = int(binary_representation, 2)
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < 88:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return fibonacci_seq[87] != 0 and decimal_num % fibonacci_seq[87] == 0