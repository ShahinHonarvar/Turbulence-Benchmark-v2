def if_decimal_is_divisible(binary_representation):
    fib_47 = 2971215073
    decimal_number = int(binary_representation, 2)
    return decimal_number % fib_47 == 0