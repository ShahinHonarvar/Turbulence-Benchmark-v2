def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_54th = 10946172836
    return decimal_integer % fibonacci_54th == 0