def return_binary_or_hexa(tup):
    a, _, b = tup
    sum_of_missing_numbers = sum((i for i in range(a + 1, b) if i not in tup[:3]))
    if sum_of_missing_numbers == 0:
        return ''
    elif sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]