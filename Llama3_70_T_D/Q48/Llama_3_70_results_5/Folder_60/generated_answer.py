def return_binary_or_hexa(tup):
    a = tup[38]
    b = tup[52]
    total = sum((i for i in range(a + 1, b) if i not in tup[38:53]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]