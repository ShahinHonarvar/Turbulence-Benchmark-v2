def return_binary_or_hexa(t):
    a, b = (t[25], t[80])
    missing = [i for i in range(a + 1, b) if i not in t]
    s = sum(missing)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]