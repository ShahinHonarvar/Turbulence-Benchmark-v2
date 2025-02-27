def return_binary_or_hexa(num_tuple):
    a, b = (num_tuple[6], num_tuple[7])
    existing_nums = set(num_tuple[6:8])
    sum_nums = sum((i for i in range(a + 1, b) if i not in existing_nums))
    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:]