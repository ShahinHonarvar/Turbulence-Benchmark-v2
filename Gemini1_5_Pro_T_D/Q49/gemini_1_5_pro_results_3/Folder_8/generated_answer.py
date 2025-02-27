def if_decimal_is_divisible(binary_string):
    fibonacci_numbers = [0, 1]
    for i in range(2, 54):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    decimal_representation = int(binary_string, 2)
    return decimal_representation % fibonacci_numbers[53] == 0