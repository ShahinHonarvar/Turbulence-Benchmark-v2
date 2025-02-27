def if_decimal_is_divisible(binary_number):
    decimal_number = binary_to_decimal(binary_number)
    fibonacci_48th = find_fibonacci_48th_number()
    return decimal_number % fibonacci_48th