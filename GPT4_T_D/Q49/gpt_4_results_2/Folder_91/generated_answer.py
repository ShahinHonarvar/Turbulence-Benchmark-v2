def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 6):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    sixth_fibonacci_number = fibonacci_sequence[5]
    if decimal_integer % sixth_fibonacci_number == 0:
        return True
    else:
        return False