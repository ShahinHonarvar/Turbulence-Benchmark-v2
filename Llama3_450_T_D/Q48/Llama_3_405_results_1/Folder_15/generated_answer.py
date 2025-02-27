def return_binary_or_hexa(t):
    a, b = (t[0], t[4])
    total = sum((i for i in range(a + 1, b) if i not in t[:5]))
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]