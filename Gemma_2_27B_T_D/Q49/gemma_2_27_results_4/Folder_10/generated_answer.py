def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_88 = 1146884518103387582295246905921715
    return decimal_number % fibonacci_88 == 0