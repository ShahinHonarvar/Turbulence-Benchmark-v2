def if_decimal_is_divisible(binary_representation):
    binary_representation = binary_representation.zfill(66)
    x, f = (0, 1)
    for i in range(len(binary_representation)):
        f, x = (x + f, f)
        if str(x)[-1] == '0' and int(binary_representation[i], 2) == 0:
            if str(f)[-1] == '0' and int(binary_representation[i], 2) == 0:
                return True
        elif str(x)[-1] == '1' and int(binary_representation[i], 2) == 1:
            if str(f)[-1] == '1' and int(binary_representation[i], 2) == 1:
                while True:
                    f, x = (x + f, f)
                    if str(f)[-1] != '0' or str(f)[-1] != '1':
                        if int(binary_representation[i + 1], 2) == int(str(f)[-1], 10):
                            return True
    return False