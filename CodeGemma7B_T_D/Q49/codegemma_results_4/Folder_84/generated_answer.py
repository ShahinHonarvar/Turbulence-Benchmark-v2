def if_decimal_is_divisible(n):
    curr, nextt = (0, 1)
    fibs = [0]
    while nextt <= 2 ** 69:
        fibs.append(nextt)
        curr, nextt = (nextt, curr + nextt)
    while fibs[-1] <= int(n, 2):
        fibs.append(fibs[-1] + fibs[-2])
    if fibs[-1] == int(n, 2):
        return True
    else:
        return False