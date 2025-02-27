def return_binary_or_hexa(tup):
    if len(tup) <= 87:
        return ''
    a, b = (tup[42], tup[87])
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[43:87]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]