def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    an = [0, 1]
    while len(an) <= 184:
        an.append(an[-2] + an[-1])
    if n % an[184] == 0:
        return True
    else:
        return False