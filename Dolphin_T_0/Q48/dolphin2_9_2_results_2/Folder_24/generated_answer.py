def return_binary_or_hexa(t):
    a = t[13]
    b = t[91]
    present = set(t[13:92])
    total = sum(range(a + 1, b))
    missing = total - sum(present)
    if missing % 2 == 1:
        return bin(missing)[2:]
    else:
        return hex(missing)[2:].upper()