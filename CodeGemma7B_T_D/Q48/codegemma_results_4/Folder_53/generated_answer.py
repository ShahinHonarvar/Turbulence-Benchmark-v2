def return_binary_or_hexa(tup):
    a, b = (tup[200], tup[202])
    s = 0
    for i in range(a + 1, b):
        if i not in tup[200:202]:
            s += i
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()