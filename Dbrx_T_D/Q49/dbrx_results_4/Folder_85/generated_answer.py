def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_number > 45:
            break
        fibonacci_sequence.append(next_number)
    return decimal_integer % 45 == 0 if len(fibonacci_sequence) >= 45 else False