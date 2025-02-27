def return_binary_or_hexa(tup):
    a, b = (tup[44], tup[91])
    present = set(tup[44 + 1:92])
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total == 0:
        return ''
    return bin(total)[2:] if total & 1 else hex(total)[2:]