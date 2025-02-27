def if_decimal_is_divisible(binary_num):
    n = int(binary_num, 2)
    a, b = (0, 1)
    for _ in range(159):
        a, b = (b, a + b)
    if n % b == 0:
        return True
    else:
        return False