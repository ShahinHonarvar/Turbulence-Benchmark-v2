def return_binary_or_hexa(t):
    a = t[32]
    b = t[44]
    total = sum(range(a + 1, b))
    diff = total - sum(t[33:44])
    if diff % 2 != 0:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]