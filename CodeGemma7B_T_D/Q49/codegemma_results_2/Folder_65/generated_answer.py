def if_decimal_is_divisible(binary):
    FIB = [0]
    p = 1
    while p <= 127:
        FIB.append(FIB[-1] + FIB[-2])
        p += 1
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    if decimal % FIB[127] == 0:
        return True
    else:
        return False