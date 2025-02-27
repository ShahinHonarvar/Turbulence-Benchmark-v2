def return_binary_or_hexa(t):
    a = t[45]
    b = t[48]
    missing = [i for i in range(a + 1, b) if i not in t[45:49]]
    s = sum(missing)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]