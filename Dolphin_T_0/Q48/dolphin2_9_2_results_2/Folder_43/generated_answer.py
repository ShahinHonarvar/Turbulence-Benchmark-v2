def return_binary_or_hexa(t):
    a = t[10]
    b = t[28]
    x = set(range(a + 1, b))
    y = set(t[10:29])
    s = x - y
    sum_s = sum(s)
    if sum_s % 2 != 0:
        return bin(sum_s)[2:]
    else:
        return hex(sum_s)[2:]