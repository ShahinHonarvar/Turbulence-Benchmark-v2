def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_numbers = [0, 1]
    for i in range(2, 186):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return decimal_number % fibonacci_numbers[185] == 0