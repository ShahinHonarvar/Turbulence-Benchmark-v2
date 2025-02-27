def return_binary_or_hexa(tup):
    a = tup[3]
    b = tup[9]
    total = sum(range(a + 1, b)) - sum((x for x in tup[4:9] if a < x < b))
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]