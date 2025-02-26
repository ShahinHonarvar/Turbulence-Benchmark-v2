def return_binary_or_hexa(tup):
    a = tup[3]
    b = tup[8]
    excluded = set(tup[3:9])
    total = sum((x for x in range(a + 1, b) if x not in excluded))
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].rstrip('L')