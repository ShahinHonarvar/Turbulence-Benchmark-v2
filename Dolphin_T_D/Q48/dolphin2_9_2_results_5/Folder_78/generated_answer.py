def return_binary_or_hexa(t):
    a = t[62]
    b = t[96]
    total = 0
    for i in range(a + 1, b):
        if i not in t[62:97]:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:]
    else:
        return ''