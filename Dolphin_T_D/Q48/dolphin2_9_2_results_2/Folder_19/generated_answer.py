def return_binary_or_hexa(t):
    a, b = (t[1], t[4])
    present = t[1:4]
    if a + 1 > b:
        return ''
    total = sum((x for x in range(a + 1, b) if x not in present))
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]