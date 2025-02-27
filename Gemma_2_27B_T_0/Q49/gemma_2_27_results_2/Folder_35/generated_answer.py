def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_187 = 10946177117890625
    return decimal_number % fibonacci_187 == 0