def return_binary_or_hexa(t):
    a = t[34]
    b = t[69]
    s = 0
    for i in t[34:70]:
        if i != a and i != b:
            s += i
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]