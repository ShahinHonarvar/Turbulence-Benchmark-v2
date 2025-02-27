def return_binary_or_hexa(t):
    a = t[2]
    b = t[8]
    present_numbers = t[2:8]
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in present_numbers))
    result = ''
    if sum_of_missing % 2 == 1:
        result = bin(sum_of_missing)[2:]
    else:
        result = hex(sum_of_missing)[2:].upper()
    return result if sum_of_missing != 0 else ''