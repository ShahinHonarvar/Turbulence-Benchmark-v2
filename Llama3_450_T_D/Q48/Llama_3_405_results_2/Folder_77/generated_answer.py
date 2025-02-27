def return_binary_or_hexa(tup):
    a = tup[18]
    b = tup[52]
    total_sum = sum((i for i in range(a + 1, b) if i not in tup[19:52]))
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    elif total_sum > 0:
        return hex(total_sum)[2:]
    else:
        return ''