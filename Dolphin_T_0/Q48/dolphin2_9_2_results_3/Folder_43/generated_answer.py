def return_binary_or_hexa(t):
    a, b = (t[10], t[28])
    total = sum(range(a + 1, b)) - sum(t[11:28])
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]