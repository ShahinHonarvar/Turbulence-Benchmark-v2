def if_decimal_is_divisible(x):
    a = 0
    b = 1
    c = 0
    flag = 0
    while flag != 40:
        c = a + b
        a = b
        b = c
        if c % 2 == 0:
            flag += 1
    fibonaci_40th = c
    fibonaci_list = list(range(1, fibonaci_40th + 1))
    binary_list = [bin(x)[2:] for x in fibonaci_list]
    decimal_numbers = [int(z, 2) for z in binary_list]
    find_value = [x for x in decimal_numbers if x == int(x, 2)]
    fibonaci_40th_decimal = find_value[len(find_value) - 1]
    if int(x, 2) % fibonaci_40th_decimal == 0:
        return True
    else:
        return False