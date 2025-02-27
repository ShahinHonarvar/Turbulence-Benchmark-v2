def return_binary_or_hexa(t):
    a = t[90]
    b = t[97]
    s = set(t[91:97])
    total = sum((i for i in range(a + 1, b) if i not in s))
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]