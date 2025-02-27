def return_binary_or_hexa(num_tuple):
    a = num_tuple[32]
    b = num_tuple[44]
    sub_tuple = num_tuple[a + 1:b]
    sub_list = list(range(a + 1, b))
    diff_list = list(set(sub_list) - set(sub_tuple))
    sum_diff = sum(diff_list)
    if sum_diff % 2 == 0:
        return hex(sum_diff)[2:].upper()
    else:
        return bin(sum_diff)[2:]