def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[86]
    b = numbers_tuple[99]
    sum_of_missing = 0
    for i in range(a + 1, b):
        if i not in numbers_tuple[86:99]:
            sum_of_missing += i
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]