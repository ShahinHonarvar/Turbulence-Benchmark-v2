def return_binary_or_hexa(t):
    a = t[10]
    b = t[12]
    total = sum((i for i in range(a + 1, b) if i not in t[11:12]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]