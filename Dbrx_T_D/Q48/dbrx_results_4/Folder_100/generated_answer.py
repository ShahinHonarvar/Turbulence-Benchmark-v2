def return_binary_or_hexa(tup):
    a, b = (tup[44], tup[78])
    present_numbers = set(tup[44:78 + 1])
    sum_of_missing = 0
    for num in range(a + 1, b):
        if num not in present_numbers:
            sum_of_missing += num
    if sum_of_missing % 2 == 0:
        return format(sum_of_missing, 'x')
    else:
        return format(sum_of_missing, 'b')