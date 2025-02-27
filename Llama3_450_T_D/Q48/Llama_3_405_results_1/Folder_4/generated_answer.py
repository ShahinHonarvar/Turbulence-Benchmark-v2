def return_binary_or_hexa(tup):
    a = tup[49]
    b = tup[74]
    total_sum = sum((i for i in range(a + 1, b) if i not in tup[49:75]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]