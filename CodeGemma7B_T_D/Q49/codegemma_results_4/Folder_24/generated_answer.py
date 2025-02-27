def if_decimal_is_divisible(binary_representation):
    a = [0, 1]
    for i in range(2, 145):
        a.append(a[i - 1] + a[i - 2])
    decimal_value = 0
    for digit in binary_representation:
        decimal_value = decimal_value * 2 + int(digit)
    if decimal_value % a[144] == 0:
        return True
    else:
        return False