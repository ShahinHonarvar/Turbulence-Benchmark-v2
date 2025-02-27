def return_binary_or_hexa(t):
    a = t[35]
    b = t[64]
    total = sum(range(a + 1, b))
    for i in t[35:64 + 1]:
        total -= i
    if not total:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()