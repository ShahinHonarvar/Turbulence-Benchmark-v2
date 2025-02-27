def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fibonacci_10th = 34
    return decimal % fibonacci_10th == 0