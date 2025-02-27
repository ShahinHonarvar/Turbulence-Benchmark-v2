def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_77 = 5527939700884757
    return decimal_number % fibonacci_77 == 0