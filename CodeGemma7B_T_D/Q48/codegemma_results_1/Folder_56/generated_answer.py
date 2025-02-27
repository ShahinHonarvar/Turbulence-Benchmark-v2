def return_binary_or_hexa(t):
    a = t[7]
    b = t[9]
    res = 0
    for i in range(a + 1, b + 1):
        if not i in t[7:9]:
            res += i
    if res % 2 == 0:
        return f'{res:x}'
    else:
        return f'{res:b}'