def return_binary_or_hexa(t):
    a = t[15]
    b = t[57]
    missing = [i for i in range(a + 1, b) if i not in t[16:57]]
    s = sum(missing)
    if s % 2 != 0:
        return bin(s).replace('0b', '')
    else:
        return hex(s).replace('0x', '').upper()