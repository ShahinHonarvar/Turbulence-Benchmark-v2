def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fibonacci_seq = [0, 1]
    for _ in range(107):
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return decimal_integer % fibonacci_seq[108] == 0