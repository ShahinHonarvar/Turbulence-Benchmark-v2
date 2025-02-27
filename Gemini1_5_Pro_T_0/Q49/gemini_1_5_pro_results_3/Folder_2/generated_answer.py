def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    a = 0
    b = 1
    count = 2
    while count < 125:
        next_fibonacci = a + b
        a = b
        b = next_fibonacci
        count += 1
    return decimal_representation % b == 0