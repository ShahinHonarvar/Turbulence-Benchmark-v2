def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[91]
    total_sum = sum((i for i in range(a + 1, b) if i not in tup[45:91]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]