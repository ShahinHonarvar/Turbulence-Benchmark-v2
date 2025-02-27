def if_decimal_is_divisible(binary_string):
    fibonacci_numbers = [0, 1]
    for i in range(2, 88):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci_numbers[87] == 0