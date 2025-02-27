def return_binary_or_hexa(tup):
    a = tup[3]
    b = tup[8]
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()