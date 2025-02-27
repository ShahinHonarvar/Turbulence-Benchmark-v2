def return_binary_or_hexa(tup):
    a = tup[77]
    b = tup[84]
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[78:84]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:]