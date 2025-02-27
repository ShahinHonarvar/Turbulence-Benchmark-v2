def return_binary_or_hexa(tup):
    a = tup[49]
    b = tup[74]
    total_sum = sum((i for i in range(a + 1, b) if i not in tup[50:74]))
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]