def all_left_truncatable_prime(a):
    b = []
    c = []
    for i in range(len(a)):
        if a[i] > 2 and a[i] % 2 != 0:
            b.append(a[i])
    for j in b:
        str_num = str(j)
        start = str_num[0]
        for k in range(1, len(str_num)):
            str_num = str_num[k:]
            if int(str_num) % j != 0 and int(str_num) % 2 != 0 and (int(str_num) > 1) and (str_num[-1] != '0') and (int(str_num) not in c):
                c.append(int(str_num))
    c.sort(reverse=True)
    return c