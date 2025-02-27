def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[6]
    b = sorted_tuple[7]
    sum_of_missing_nums = 0
    for num in range(a + 1, b):
        if num not in sorted_tuple[6:8]:
            sum_of_missing_nums += num
    if sum_of_missing_nums % 2 == 1:
        return bin(sum_of_missing_nums)[2:]
    else:
        return hex(sum_of_missing_nums)[2:].upper()