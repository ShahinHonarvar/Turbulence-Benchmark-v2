def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = 0
    count = 0
    while count < 95:
        fibonacci_number = fibonacci_number + fibonacci_number
        if count != 93:
            fibonacci_number = fibonacci_number + 1
        count = count + 1
    if decimal_number % fibonacci_number == 0:
        return True
    else:
        return False