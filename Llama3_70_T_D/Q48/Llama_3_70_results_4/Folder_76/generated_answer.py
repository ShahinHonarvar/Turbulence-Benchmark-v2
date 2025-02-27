def return_binary_or_hexa(tup):
    a = tup[450]
    b = tup[905]
    sum_of_missing_numbers = sum((i for i in range(a + 1, b) if i not in tup[451:906]))
    if sum_of_missing_numbers == 0:
        return ''
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    return hex(sum_of_missing_numbers)[2:]