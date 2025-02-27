def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fibonacci_68 = 2971215073
    return decimal_number % fibonacci_68 == 0