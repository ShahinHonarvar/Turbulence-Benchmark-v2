def return_binary_or_hexa(t):
    a = t[44]
    b = t[78]
    s = set(t[45:79])
    total = sum((i for i in range(a + 1, b) if i not in s))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]