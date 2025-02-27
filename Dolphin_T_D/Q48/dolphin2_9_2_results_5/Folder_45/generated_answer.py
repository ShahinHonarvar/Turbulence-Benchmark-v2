def return_binary_or_hexa(t):
    a = t[30]
    b = t[200]
    present = all((x in t[30:201] for x in range(a + 1, b, 1)))
    if present:
        return ''
    sum = 0
    for x in range(a + 1, b, 1):
        if x not in t[30:201]:
            sum += x
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]