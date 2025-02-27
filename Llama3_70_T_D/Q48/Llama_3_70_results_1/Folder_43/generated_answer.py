def return_binary_or_hexa(t):
    a = t[10]
    b = t[28]
    total = sum((i for i in range(a + 1, b) if i not in t[10:29]))
    if total % 2 != 0:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:]
    else:
        return ''