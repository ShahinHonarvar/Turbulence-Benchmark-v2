def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_109 = 2880067194370816120
    return decimal % fib_109 == 0