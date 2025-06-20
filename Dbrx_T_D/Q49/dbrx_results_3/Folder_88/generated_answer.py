def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = 0
    previous_number = 0
    current_number = 1
    while fibonacci_number < decimal_number:
        fibonacci_number = previous_number + current_number
        previous_number = current_number
        current_number = fibonacci_number
    return decimal_number % fibonacci_number == 0