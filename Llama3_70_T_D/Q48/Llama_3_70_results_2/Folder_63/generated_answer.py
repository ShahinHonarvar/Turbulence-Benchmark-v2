def return_binary_or_hexa(tup):
    a = tup[81]
    b = tup[86]
    sum_of_missing_numbers = sum((i for i in range(a + 1, b) if i not in tup[81:87]))
    if sum_of_missing_numbers == 0:
        return ''
    elif sum_of_missing_numbers % 2 != 0:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]