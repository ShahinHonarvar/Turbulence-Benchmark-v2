def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    if decimal == 0:
        return False
    if decimal == 1:
        return True
    else:
        a, b, i = (0, 1, 1)
        while i < 190:
            a, b = (b, a + b)
            i += 1
        return decimal % b == 0