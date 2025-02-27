def return_binary_or_hexa(num_tuple):
    a = num_tuple[86]
    b = num_tuple[90]
    if all((num in num_tuple for num in range(a + 1, b))):
        return ''
    else:
        sum_missing = sum(set(range(a + 1, b)) - set(num_tuple[87:90]))
        if sum_missing % 2 == 0:
            return hex(sum_missing)[2:]
        else:
            return bin(sum_missing)[2:]