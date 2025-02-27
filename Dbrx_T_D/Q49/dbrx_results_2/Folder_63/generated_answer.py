def if_decimal_is_divisible(bin_repr: str) -> bool:
    decimal = int(bin_repr, 2)
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < 144:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return decimal % fibonacci_seq[143] == 0 if decimal > 0 else False