def return_binary_or_hexa(tup):
    a = tup[32]
    b = tup[44]
    present_set = set(tup[32:45])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_set))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()