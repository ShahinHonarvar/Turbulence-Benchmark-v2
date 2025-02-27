def find_mid(num):
    tmp = []
    while num:
        if num % 2:
            tmp.append(1)
        else:
            tmp.append(0)
        num //= 2
    return tmp