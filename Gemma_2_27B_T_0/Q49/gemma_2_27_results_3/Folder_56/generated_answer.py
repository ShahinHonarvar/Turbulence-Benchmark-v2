def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_84 = 1809979701768707007
    return decimal_number % fibonacci_84 == 0