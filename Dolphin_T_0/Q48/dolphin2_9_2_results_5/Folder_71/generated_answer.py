def return_binary_or_hexa(input_tuple):
    a = input_tuple[20]
    b = input_tuple[35]
    all_nums = set(input_tuple)
    subset = all_nums & set(range(a + 1, b))
    missing = set(range(a + 1, b + 1)) - subset
    sum_num = sum(missing)
    if sum_num % 2 != 0:
        return bin(sum_num)[2:]
    else:
        return hex(sum_num)[2:]