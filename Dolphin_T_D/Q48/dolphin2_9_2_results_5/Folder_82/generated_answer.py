def return_binary_or_hexa(t):
    a = t[20]
    b = t[200]
    s = set(t[21:200])
    res = 0
    for i in range(a + 1, b):
        if i not in s:
            res += i
    if res % 2:
        return bin(res)[2:]
    else:
        return hex(res)[2:]