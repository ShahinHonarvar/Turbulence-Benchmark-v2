def return_binary_or_hexa(tup):
    a = tup[37]
    b = tup[43]
    excluded_range = set(tup[37:44])
    sum_excluded = sum((num for num in range(a + 1, b) if num not in excluded_range))
    if sum_excluded == 0:
        return ''
    elif sum_excluded % 2 == 1:
        return bin(sum_excluded)[2:]
    else:
        return hex(sum_excluded)[2:]