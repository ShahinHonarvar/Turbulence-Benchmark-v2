def return_binary_or_hexa(t):
    a = t[10]
    b = t[100]
    excluded = set(t[10:101])
    total = sum((i for i in range(a + 1, b) if i not in excluded))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]