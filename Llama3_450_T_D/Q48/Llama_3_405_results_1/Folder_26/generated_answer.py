def return_binary_or_hexa(tup):
    a = tup[68]
    b = tup[99]
    tup_set = set(tup[68:100])
    total_sum = sum((i for i in range(a + 1, b) if i not in tup_set))
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    elif total_sum > 0:
        return hex(total_sum)[2:]
    else:
        return ''