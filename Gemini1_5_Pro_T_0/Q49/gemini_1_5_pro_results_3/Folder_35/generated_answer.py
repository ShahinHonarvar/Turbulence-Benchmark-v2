def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    fibonacci_numbers = [0, 1]
    for i in range(2, 187):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return decimal_representation % fibonacci_numbers[186] == 0