def return_binary_or_hexa(num_tuple):
    a, b = (num_tuple[37], num_tuple[43])
    sum_of_missing_nums = sum(set(range(a + 1, b)) - set(num_tuple[37:44]))
    if sum_of_missing_nums % 2 != 0:
        return bin(sum_of_missing_nums)[2:]
    else:
        return hex(sum_of_missing_nums)[2:].upper()