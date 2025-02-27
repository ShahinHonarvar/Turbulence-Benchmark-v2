def return_binary_or_hexa(tup):
    a, b = (tup[38], tup[81])
    sum_not_present = sum((x for x in range(a + 1, b) if x not in tup[38:82]))
    if sum_not_present % 2:
        return bin(sum_not_present).split('0b')[-1]
    else:
        return hex(sum_not_present).split('0x')[-1].upper()