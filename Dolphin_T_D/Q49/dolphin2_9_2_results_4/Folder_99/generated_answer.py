def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci_seq = [0, 1]
    i = 2
    while fibonacci_seq[i - 1] < decimal:
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])
        i += 1
    return decimal % fibonacci_seq[108] == 0