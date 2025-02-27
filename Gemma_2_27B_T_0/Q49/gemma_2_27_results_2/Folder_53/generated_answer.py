def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_64 = 10610209857723
    return decimal_value % fibonacci_64 == 0