def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    fib127 = 198343720
    return decimal_representation % fib127 == 0