def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_164 = 10610209857723
    return decimal_number % fibonacci_164 == 0