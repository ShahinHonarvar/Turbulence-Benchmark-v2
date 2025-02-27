def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[73]
    b = sorted_tuple[84]
    missing_sum = sum((i for i in range(a + 1, b) if i not in sorted_tuple[73:85]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]