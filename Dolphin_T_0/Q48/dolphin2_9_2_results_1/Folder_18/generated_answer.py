def missing_in_range(a, b):
    missing = []
    for i in range(a + 1, b):
        if i not in my_list[index_a:index_b]:
            missing.append(i)
    return missing

def return_binary_or_hexa(my_list):
    index_a = 56
    index_b = 90
    a = my_list[index_a]
    b = my_list[index_b]
    missing_numbers = missing_in_range(a, b)
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]