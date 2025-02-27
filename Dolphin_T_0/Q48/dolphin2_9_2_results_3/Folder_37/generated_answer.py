def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    if all((x in t[2:8] for x in range(a + 1, b))):
        return ''
    total = 0
    for x in range(a + 1, b):
        if x not in t[2:8]:
            total += x
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]