def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibf = [0, 1]
    for i in range(2, 176):
        fibf.append(fibf[i - 1] + fibf[i - 2])
    if decimal % fibf[175] == 0:
        return True
    else:
        return False