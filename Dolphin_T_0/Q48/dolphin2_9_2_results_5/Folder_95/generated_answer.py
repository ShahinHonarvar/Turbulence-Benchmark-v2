def return_binary_or_hexa(t):
    a = t[32]
    b = t[99]
    total = 0
    for x in range(a + 1, b):
        if x not in t:
            total += x
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]