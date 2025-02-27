def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[8]
    total = sum((i for i in range(a + 1, b) if i not in tup[1:9]))
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    return hex(total)[2:]