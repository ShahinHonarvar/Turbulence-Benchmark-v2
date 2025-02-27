def return_binary_or_hexa(tup):
    a, b = (tup[200], tup[202])
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[200:203]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]