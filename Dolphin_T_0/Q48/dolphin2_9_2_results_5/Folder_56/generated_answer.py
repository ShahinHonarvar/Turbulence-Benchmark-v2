def return_binary_or_hexa(t):
    a, b = (t[7], t[9])
    total = sum(set(range(a + 1, b)) - set(t[8:] or t[10:] or []))
    if total == 0:
        return ''
    elif total & 1:
        return bin(total).replace('0b', '')
    else:
        return hex(total).replace('0x', '').upper()