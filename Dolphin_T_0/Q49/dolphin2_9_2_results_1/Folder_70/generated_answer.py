def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci137 = [0, 1]
    for i in range(2, 137):
        fibonacci137.append(fibonacci137[i - 1] + fibonacci137[i - 2])
    if fibonacci137[-1] != 0 and decimal % fibonacci137[-1] == 0:
        return True
    else:
        return False