def return_binary_or_hexa(t):
    a = t[57]
    b = t[84]
    if all((x in t for x in range(a + 1, b))):
        return ''
    sum = 0
    for x in range(a + 1, b):
        if x not in t:
            sum += x
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]