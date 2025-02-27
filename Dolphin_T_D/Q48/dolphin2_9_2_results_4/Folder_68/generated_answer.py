def return_binary_or_hexa(t):
    a = t[0]
    b = t[9]
    total = sum(range(a + 1, b))
    for i in t:
        if a < i < b:
            total -= i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()