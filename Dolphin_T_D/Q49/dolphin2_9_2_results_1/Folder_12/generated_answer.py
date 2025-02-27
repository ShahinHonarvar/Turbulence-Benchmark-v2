def if_decimal_is_divisible(binary_representation):
    num_fibonacci = 0
    a, b = (0, 1)
    while num_fibonacci < 66:
        a, b = (b, a + b)
        num_fibonacci += 1
    decimal_value = int(binary_representation, 2)
    return decimal_value % a == 0