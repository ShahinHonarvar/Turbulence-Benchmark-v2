def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    a = 0
    b = 1
    for i in range(84):
        temp = a
        a = b
        b = temp + b
    if decimal_representation % a == 0:
        return True
    else:
        return False