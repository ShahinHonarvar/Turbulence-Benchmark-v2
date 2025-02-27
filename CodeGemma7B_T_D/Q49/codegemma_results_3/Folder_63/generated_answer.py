def if_decimal_is_divisible(binary_string):
    length_binary_string = len(binary_string)
    fibonacci_sequence = [0, 1]
    for i in range(2, 144):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    decimal_integer = 0
    for i, digit in enumerate(binary_string):
        decimal_integer += int(digit) * 2 ** (length_binary_string - i - 1)
    if decimal_integer % fibonacci_sequence[143] == 0:
        return True
    else:
        return False