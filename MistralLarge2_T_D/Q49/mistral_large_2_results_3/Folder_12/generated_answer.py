def if_decimal_is_divisible(binary_representation):
    fib_66 = 17711
    decimal_value = int(binary_representation, 2)
    return decimal_value % fib_66 == 0