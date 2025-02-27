def return_binary_or_hexa(num_tuple):
    a = num_tuple[33]
    b = num_tuple[78]
    missing_nums = [i for i in range(a + 1, b) if i not in num_tuple[33:79]]
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]