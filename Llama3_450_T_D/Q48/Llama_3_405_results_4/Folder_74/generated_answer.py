def return_binary_or_hexa(tup):
    a = tup[69]
    b = tup[97]
    total_sum = sum((i for i in range(a + 1, b) if i not in tup[69:97]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]