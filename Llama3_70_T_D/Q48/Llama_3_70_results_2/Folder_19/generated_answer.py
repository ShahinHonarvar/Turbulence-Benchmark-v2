def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[4]
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[1:5]))
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:]