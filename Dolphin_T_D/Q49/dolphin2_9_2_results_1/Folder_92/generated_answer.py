def if_decimal_is_divisible(binary_representation):
    fibonacci_numbers = [0, 1]
    decimal_number = 0
    binary_digit_value = 1
    for digit in reversed(binary_representation):
        if digit == '1':
            decimal_number += binary_digit_value
        binary_digit_value *= 2
    while len(fibonacci_numbers) <= 7:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return decimal_number % fibonacci_numbers[-1] == 0