def return_binary_or_hexa(tup):
    a = tup[68]
    b = tup[99]
    total = sum((i for i in range(a + 1, b) if i not in tup[68:100]))
    if total % 2 == 1:
        return bin(total)[2:]
    elif total == 0:
        return ''
    else:
        return hex(total)[2:]