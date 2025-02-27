def return_binary_or_hexa(t):
    a = t[44]
    b = t[78]
    present = set(t[45:78])
    total = sum(range(a + 1, b))
    not_present = total - sum(present)
    if not_present % 2:
        return bin(not_present)[2:]
    else:
        return hex(not_present)[2:]