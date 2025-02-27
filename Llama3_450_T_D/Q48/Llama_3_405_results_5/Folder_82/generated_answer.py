def return_binary_or_hexa(t):
    a = t[20]
    b = t[200]
    s = set(t[20:201])
    total = sum((i for i in range(a + 1, b) if i not in s))
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]