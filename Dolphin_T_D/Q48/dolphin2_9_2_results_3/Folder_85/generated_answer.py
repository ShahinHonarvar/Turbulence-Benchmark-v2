def return_binary_or_hexa(t):
    a = t[1]
    b = t[8]
    l = [x for x in range(a + 1, b) if x not in t]
    total = sum(l)
    if total:
        if total % 2:
            return bin(total)[2:]
        else:
            return hex(total)[2:].upper()
    else:
        return ''