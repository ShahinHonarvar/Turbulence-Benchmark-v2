def return_binary_or_hexa(data):
    a, b = (data[57], data[84])
    range_set = set(range(a + 1, b))
    missing_sum = sum((x for x in range_set if x not in data[57:85]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]