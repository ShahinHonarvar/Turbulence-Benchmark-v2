def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    fibonacci_numbers = [0, 1]
    for i in range(2, 189):
        next_fibonacci_number = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
        fibonacci_numbers.append(next_fibonacci_number)
    return decimal_representation % fibonacci_numbers[188] == 0