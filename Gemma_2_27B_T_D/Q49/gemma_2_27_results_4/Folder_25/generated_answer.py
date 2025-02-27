def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fibonacci_19 = 4181
    return decimal_number % fibonacci_19 == 0