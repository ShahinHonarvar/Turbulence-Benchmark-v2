def if_decimal_is_divisible(binary_string):
    fibonacci_seq = [0, 1]
    for i in range(2, 190):
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci_seq[189] == 0