def if_decimal_is_divisible(a):
    b, c = (0, 1)
    flag = 1
    while True:
        d = b + c
        if d > 114:
            if flag == 1:
                flag = 0
            else:
                return False
        elif d == 114:
            flag = 0
        b, c = (c, d)
        if len(str(a)) == len(str(d)):
            if int(str(a)) % int(str(d)) == 0:
                return True