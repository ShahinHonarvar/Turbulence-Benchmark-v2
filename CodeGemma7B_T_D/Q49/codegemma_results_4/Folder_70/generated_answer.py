def if_decimal_is_divisible(binary_no):
    first, second = (0, 1)
    for i in range(int(binary_no)):
        first, second = (second, first + second)
    return (first + int(binary_no)) % 137 == 0