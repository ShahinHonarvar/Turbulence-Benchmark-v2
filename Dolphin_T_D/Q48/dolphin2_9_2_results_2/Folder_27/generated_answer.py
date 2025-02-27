def return_binary_or_hexa(lst):
    start_index = 86
    end_index = 89
    a = lst[start_index]
    b = lst[end_index]
    missing_nums = [i for i in range(a + 1, b) if i not in lst[start_index:end_index + 1]]
    sum_of_missing = sum(missing_nums)
    if sum_of_missing % 2 != 0:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()