def if_decimal_is_divisible(binary_string):
    decimal_representation = int(binary_string, 2)
    fibonacci_numbers = [0, 1]
    for i in range(2, 78):
        next_fibonacci_number = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
        fibonacci_numbers.append(next_fibonacci_number)
    return decimal_representation % fibonacci_numbers[77] == 0