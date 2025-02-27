def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < 196:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return decimal % fibonacci_seq[195] == 0