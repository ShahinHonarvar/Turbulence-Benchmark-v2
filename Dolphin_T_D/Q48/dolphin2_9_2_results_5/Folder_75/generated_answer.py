def return_binary_or_hexa(tuple):
    a = tuple[20]
    b = tuple[51]
    summ = sum(set(range(a + 1, b)) - set(tuple[20:52]))
    if summ % 2 != 0:
        return bin(summ).replace('0b', '')
    else:
        return hex(summ).replace('0x', '').upper()