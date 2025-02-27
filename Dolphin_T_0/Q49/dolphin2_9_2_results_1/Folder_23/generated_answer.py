def if_decimal_is_divisible(binary_number):
    decimal_number = int(binary_number, 2)
    fibonacci_seq = [0, 1]
    for i in range(2, 48):
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])
    return fibonacci_seq[47] != 0 and decimal_number % fibonacci_seq[47] == 0