def return_binary_or_hexa(tup):
    a = tup[450]
    b = tup[905]
    tup_set = set(tup[451:905])
    total = sum((i for i in range(a + 1, b) if i not in tup_set))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]