def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = 0
    previous_number = -1
    current_number = 0
    count = 0
    while count < 126:
        fibonacci_number = current_number + previous_number
        previous_number = current_number
        current_number = fibonacci_number
        count += 1
    return decimal_number % fibonacci_number == 0