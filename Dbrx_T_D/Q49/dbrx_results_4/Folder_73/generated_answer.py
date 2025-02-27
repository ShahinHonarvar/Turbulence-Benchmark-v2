def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_number = 0
    for _ in range(164):
        fibonacci_number, _ = (fibonacci_number + 1, fibonacci_number)
    return decimal_integer % fibonacci_number == 0