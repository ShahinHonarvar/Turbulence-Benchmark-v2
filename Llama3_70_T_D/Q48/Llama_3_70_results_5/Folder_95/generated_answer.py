def return_binary_or_hexa(tup):
    a = tup[32]
    b = tup[99]
    total = sum((i for i in range(a + 1, b) if i not in tup[32:100]))
    if total == 0:
        return ''
    return bin(total)[2:] if total % 2 else hex(total)[2:]