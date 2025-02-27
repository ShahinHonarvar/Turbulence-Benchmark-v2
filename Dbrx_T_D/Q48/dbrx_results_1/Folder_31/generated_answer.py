def return_binary_or_hexa(t):
    a, b = (t[33], t[78])
    sum_not_present = sum((i for i in range(a + 1, b) if i not in t[33:79]))
    if sum_not_present % 2:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()