def return_binary_or_hexa(t):
    a, b = (t[19], t[32])
    total = sum(range(a + 1, b)) - sum(t[20:32])
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]