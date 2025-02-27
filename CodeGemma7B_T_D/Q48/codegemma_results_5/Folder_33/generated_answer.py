def return_binary_or_hexa(t):
    if len(t) <= 13:
        return ''
    a, b = (t[13], t[35])
    sum = 0
    for i in range(a + 1, b):
        if i not in t[13:36]:
            sum += i
    if sum % 2:
        return str(bin(sum))[2:]
    else:
        return str(hex(sum))[2:].upper()