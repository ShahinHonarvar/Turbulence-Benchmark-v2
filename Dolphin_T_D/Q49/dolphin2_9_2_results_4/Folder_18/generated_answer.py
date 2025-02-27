def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    list_fibonacci = [0, 1]
    for i in range(3, 200):
        list_fibonacci.append(list_fibonacci[i - 1] + list_fibonacci[i - 2])
    if decimal_integer % list_fibonacci[198] == 0:
        return True
    else:
        return False