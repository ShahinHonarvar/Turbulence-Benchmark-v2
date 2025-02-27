def return_binary_or_hexa(t):
    a = t[275]
    b = t[871]
    s = set(t[276:871])
    total = sum((i for i in range(a + 1, b) if i not in s))
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]