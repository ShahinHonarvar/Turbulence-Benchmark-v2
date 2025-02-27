def return_binary_or_hexa(tup):
    a, b = (tup[13], tup[70])
    present_set = set(tup[13:70])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_set))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]