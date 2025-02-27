def return_binary_or_hexa(t):
    a, b = (t[1], t[4])
    present = set(t[1:5])
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]