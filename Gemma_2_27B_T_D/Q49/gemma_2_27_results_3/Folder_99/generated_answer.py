def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_109 = 354224848179261915075
    if decimal_number % fibonacci_109 == 0:
        return True
    else:
        return False