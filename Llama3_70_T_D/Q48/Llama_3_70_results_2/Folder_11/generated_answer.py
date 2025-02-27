def return_binary_or_hexa(tup):
    a, b = (tup[48], tup[76])
    tup_range = set(tup[48:77])
    total_sum = sum((i for i in range(a + 1, b) if i not in tup_range))
    if total_sum == 0:
        return ''
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]