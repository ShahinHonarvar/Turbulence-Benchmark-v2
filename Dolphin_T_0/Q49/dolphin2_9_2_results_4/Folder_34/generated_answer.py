def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_seq = [0, 1]
    for n in range(2, 24):
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    if decimal_number % fibonacci_seq[-1] == 0:
        return True
    else:
        return False