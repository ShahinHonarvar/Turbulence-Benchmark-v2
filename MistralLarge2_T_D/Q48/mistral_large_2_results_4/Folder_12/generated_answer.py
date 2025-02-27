def return_binary_or_hexa(data):
    a = data[16]
    b = data[87]
    sum_missing = sum((x for x in range(a + 1, b) if x not in data[16:88]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]