def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[44]
    b = sorted_tuple[67]
    missing_sum = sum(set(range(a + 1, b)) - set(sorted_tuple[44:68]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()