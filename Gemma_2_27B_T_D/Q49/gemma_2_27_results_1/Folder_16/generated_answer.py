def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_128 = 89443943237914643
    return decimal_number % fibonacci_128 == 0