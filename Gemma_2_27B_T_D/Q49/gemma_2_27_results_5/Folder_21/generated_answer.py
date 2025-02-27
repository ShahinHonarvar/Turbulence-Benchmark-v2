def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_195 = 1267650600228229401496703205376
    return decimal_number % fibonacci_195 == 0