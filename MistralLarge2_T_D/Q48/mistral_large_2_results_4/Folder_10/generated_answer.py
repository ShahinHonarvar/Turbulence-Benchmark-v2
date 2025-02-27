def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[36]
    b = sorted_tuple[54]
    missing_sum = sum((x for x in range(a + 1, b) if x not in sorted_tuple[36:55]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]