def return_binary_or_hexa(t):
    a = t[80]
    b = t[200]
    total = sum((i for i in range(a + 1, b) if i not in t[81:201]))
    return bin(total)[2:] if total % 2 else hex(total)[2:]