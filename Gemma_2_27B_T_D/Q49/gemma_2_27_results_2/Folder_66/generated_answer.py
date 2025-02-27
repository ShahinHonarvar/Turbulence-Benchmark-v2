def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_120 = 275803187526434623586574825541840413
    return decimal % fibonacci_120 == 0