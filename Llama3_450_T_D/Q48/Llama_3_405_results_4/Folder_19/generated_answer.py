def return_binary_or_hexa(t):
    a = t[1]
    b = t[4]
    total = sum((i for i in range(a + 1, b) if i not in t[2:4]))
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]