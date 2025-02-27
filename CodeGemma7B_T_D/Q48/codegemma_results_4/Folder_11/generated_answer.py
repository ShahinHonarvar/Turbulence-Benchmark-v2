def return_binary_or_hexa(user_tuple):
    a = user_tuple[48]
    b = user_tuple[76]
    present_nums = set(user_tuple[48:77])
    missing_nums = set(range(a + 1, b)) - present_nums
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:].upper()
    else:
        return bin(sum_missing_nums)[2:]