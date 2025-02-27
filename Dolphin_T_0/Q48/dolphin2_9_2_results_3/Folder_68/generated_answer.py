def return_binary_or_hexa(t):
    a, b = (t[0], t[9])
    total = sum(range(a + 1, b)) - sum(t)
    if total == 0:
        return ''
    if total % 2 == 0:
        return hex(total)[2:]
    return bin(total)[2:]