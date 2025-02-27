def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    a = 0
    b = 1
    counter = 2
    while counter <= 174:
        temp = a + b
        a = b
        b = temp
        counter += 1
    if decimal_representation % b == 0:
        return True
    else:
        return False