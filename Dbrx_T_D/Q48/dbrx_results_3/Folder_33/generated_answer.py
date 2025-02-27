def return_binary_or_hexa(int_tuple):
    a = int_tuple[13]
    b = int_tuple[35]
    sum_set = set(range(a + 1, b))
    diff_set = sum_set.difference(int_tuple[13:35])
    sum_diff = sum(diff_set)
    if sum_diff % 2 != 0:
        return bin(sum_diff)[2:]
    else:
        return hex(sum_diff)[2:].upper()