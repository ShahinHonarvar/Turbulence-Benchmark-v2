def return_binary_or_hexa(t):
    a = t[55]
    b = t[84]
    present = set(t[56:84])
    total = sum(range(a + 1, b, 1))
    total_not_present = total - sum(present)
    if total_not_present % 2 == 1:
        return bin(total_not_present)[2:]
    else:
        return hex(total_not_present)[2:].upper()