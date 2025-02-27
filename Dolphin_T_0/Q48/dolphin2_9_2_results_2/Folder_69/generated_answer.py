def return_binary_or_hexa(t):
    a = t[39]
    b = t[43]
    if all((x in t for x in range(a + 1, b - 1))):
        return ''
    sum = 0
    for x in range(a + 1, b):
        if x not in t:
            sum += x
    if sum % 2 != 0:
        return bin(sum)[2:]
    return hex(sum)[2:]