def return_binary_or_hexa(t):
    a = t[20]
    b = t[36]
    missing = [i for i in range(a + 1, b) if i not in t[20:37]]
    s = sum(missing)
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]