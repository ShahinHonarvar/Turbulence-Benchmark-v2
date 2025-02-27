def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_values = [0, 1]
    for i in range(2, 28):
        fibonacci_values.append(fibonacci_values[i - 1] + fibonacci_values[i - 2])
    return decimal_number % fibonacci_values[26] == 0