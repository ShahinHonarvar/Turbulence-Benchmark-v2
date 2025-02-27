def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    fibonacci = [0, 1]
    for i in range(2, 165):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    if fibonacci[164] != 0 and decimal_num % fibonacci[164] == 0:
        return True
    else:
        return False