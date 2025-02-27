def return_binary_or_hexa(x):
    a, b = (x[10], x[79])
    s = 0
    for i in range(a + 1, b):
        if i not in x[10:80]:
            s += i
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()