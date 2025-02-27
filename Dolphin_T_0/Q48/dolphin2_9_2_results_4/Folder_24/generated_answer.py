def return_binary_or_hexa(t):
    a = t[13]
    b = t[91]
    present = set(t[13:92])
    total = sum((x for x in range(a + 1, b) if x not in present))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]