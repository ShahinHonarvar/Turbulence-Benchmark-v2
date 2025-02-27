def if_decimal_is_divisible(binary_rep):
    a, b = (0, 1)
    fibonacci_list = [a]
    while len(fibonacci_list) < 16:
        a, b = (b, a + b)
        fibonacci_list.append(a)
    decimal_num = int(binary_rep, 2)
    return decimal_num % fibonacci_list[15] == 0