def return_binary_or_hexa(t):
    a, b = (t[6], t[7])
    sum_not_present = sum((i for i in range(a + 1, b) if i not in t[6:8]))
    if sum_not_present % 2:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()