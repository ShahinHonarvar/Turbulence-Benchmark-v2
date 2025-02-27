def if_decimal_is_divisible(bin_string):
    bin_list = list(bin_string)
    decimal = 0
    for i in range(len(bin_list)):
        decimal += int(bin_list[i]) * 2 ** (len(bin_list) - 1 - i)
    a, b = (0, 1)
    for _ in range(109):
        a, b = (b, a + b)
    if decimal % b == 0:
        return True
    else:
        return False