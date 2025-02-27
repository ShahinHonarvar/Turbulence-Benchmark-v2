def if_decimal_is_divisible(binary):
    fibs = [0, 1]
    i = 1
    while len(fibs) < 160:
        fibs.append(fibs[i] + fibs[i - 1])
        i += 1
    dec = int(binary, 2)
    for f in fibs[158:]:
        if dec % f == 0:
            return True
    return False