def return_binary_or_hexa(t):
    a, b = (t[2], t[5])
    total = sum((i for i in range(a + 1, b) if i not in t[2:6]))
    if total == 0:
        return ''
    return bin(total)[2:] if total % 2 else hex(total)[2:]