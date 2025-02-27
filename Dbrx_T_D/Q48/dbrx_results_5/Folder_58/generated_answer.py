def return_binary_or_hexa(int_tuple):
    a = int_tuple[274]
    b = int_tuple[870]
    sum_of_missing = 0
    for i in range(a + 1, b):
        if i not in int_tuple[275:871]:
            sum_of_missing += i
    if sum_of_missing % 2 != 0:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()