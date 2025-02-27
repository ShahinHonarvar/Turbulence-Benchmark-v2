def return_binary_or_hexa(t):
    a, b = (t[48], t[76])
    sum_not_present = sum((x for x in range(a + 1, b) if x not in t[48:76]))
    if sum_not_present % 2:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()