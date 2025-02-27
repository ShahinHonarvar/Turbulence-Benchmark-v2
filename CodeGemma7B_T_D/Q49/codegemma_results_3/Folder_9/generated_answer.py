def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 68):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    for fibonacci_number in fibonacci_sequence:
        if decimal % fibonacci_number == 0:
            return True
    return False