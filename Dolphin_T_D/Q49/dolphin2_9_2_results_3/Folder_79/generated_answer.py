def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    fibonacci_num = 0
    a, b = (0, 1)
    while b < decimal_num:
        a, b = (b, a + b)
        fibonacci_num += 1
    if fibonacci_num == 13:
        return decimal_num % fibonacci_num == 0
    else:
        return False