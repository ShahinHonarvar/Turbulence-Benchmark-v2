def return_binary_or_hexa(t):
    a, b = (t[0], t[6])
    total = sum((i for i in range(a + 1, b) if i not in t[:7]))
    if total == 0:
        return ''
    return bin(total)[2:] if total % 2 else hex(total)[2:]