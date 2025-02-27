def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_128 = 1094617711930473686
    return decimal_value % fibonacci_128 == 0