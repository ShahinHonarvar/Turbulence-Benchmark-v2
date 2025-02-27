def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_seq = [0, 1]
    for i in range(2, 85):
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])
    if decimal_integer % fibonacci_seq[84] == 0:
        return True
    else:
        return False