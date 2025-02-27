def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_160 = 4839141959164955206448391419591649552064
    return decimal % fibonacci_160 == 0