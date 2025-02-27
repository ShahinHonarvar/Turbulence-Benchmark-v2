def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fibonacci_seq = [0, 1]
    for i in range(2, 196):
        fibonacci_seq.append(fibonacci_seq[-2] + fibonacci_seq[-1])
    if decimal_number % fibonacci_seq[194] == 0:
        return True
    else:
        return False