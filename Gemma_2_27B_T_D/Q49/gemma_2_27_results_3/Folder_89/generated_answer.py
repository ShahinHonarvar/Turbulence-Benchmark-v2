def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_126 = 279487132553974118879357787859064072561
    return decimal_number % fibonacci_126 == 0