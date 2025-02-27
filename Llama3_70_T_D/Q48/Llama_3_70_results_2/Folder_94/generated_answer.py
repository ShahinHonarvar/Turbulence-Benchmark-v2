def return_binary_or_hexa(tup):
    a = tup[42]
    b = tup[87]
    total = sum((i for i in range(a + 1, b) if i not in tup[42:88]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]