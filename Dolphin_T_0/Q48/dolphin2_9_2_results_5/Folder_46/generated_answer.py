def return_binary_or_hexa(t):
    a = t[10]
    b = t[79]
    missing = [i for i in range(a + 1, b) if i not in t[10:80]]
    s = sum(missing)
    if s % 2 == 0:
        return hex(s).upper()[2:]
    else:
        return bin(s)[2:]