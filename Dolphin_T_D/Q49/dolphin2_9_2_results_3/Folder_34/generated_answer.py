def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_number = 0
    i = 0
    while i < 24:
        fibonacci_number, _ = divmod(fibonacci_number + binary_string, 2)
        i += 1
    return decimal % fibonacci_number == 0