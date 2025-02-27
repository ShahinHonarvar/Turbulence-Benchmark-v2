def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_seq = [0, 1]
    for i in range(2, 177):
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])
    return decimal_integer % fibonacci_seq[176] == 0