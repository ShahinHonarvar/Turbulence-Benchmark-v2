def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci = 1
    previous_fibonacci = 0
    for i in range(45):
        fibonacci, previous_fibonacci = (fibonacci + previous_fibonacci, fibonacci)
    return decimal_integer % fibonacci == 0