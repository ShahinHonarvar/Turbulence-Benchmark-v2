def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_64 = 10610209857723
    return decimal % fibonacci_64 == 0