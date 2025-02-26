def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[5])
    sum_range = set(range(a + 1, b))
    sum_tuple = set(tup[1:5])
    missing_sum = sum(sum_range - sum_tuple)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()