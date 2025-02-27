def return_binary_or_hexa(tup):
    a = tup[43]
    b = tup[70]
    sum_of_missing_numbers = sum((i for i in range(a + 1, b) if i not in tup[43:71]))
    if sum_of_missing_numbers == 0:
        return ''
    elif sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:]
    else:
        return bin(sum_of_missing_numbers)[2:]