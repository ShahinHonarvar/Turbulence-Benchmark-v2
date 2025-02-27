def return_binary_or_hexa(t):
    a, b = (t[6], t[7])
    s = [i for i in range(a + 1, b) if i not in t]
    total = sum(s)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()