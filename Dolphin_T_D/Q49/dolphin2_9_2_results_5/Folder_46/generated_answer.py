def if_decimal_is_divisible(number_in_binary_format):
    number_in_decimal_format = int(number_in_binary_format, 2)
    fibonacci_numbers = [0, 1]
    fibonacci_index = 2
    while fibonacci_numbers[-1] <= number_in_decimal_format:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
        fibonacci_index += 1
    if number_in_decimal_format % fibonacci_numbers[138] == 0:
        return True
    return False