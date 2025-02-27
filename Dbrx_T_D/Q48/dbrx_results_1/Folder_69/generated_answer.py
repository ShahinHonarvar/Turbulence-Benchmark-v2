def return_binary_or_hexa(t):
    a, b = (t[39], t[43])
    present_set = set(t[:39] + t[44:])
    sum_of_missing = sum((x for x in range(a + 1, b) if x not in present_set))
    if sum_of_missing % 2:
        return format(sum_of_missing, '08b')
    else:
        return format(sum_of_missing, 'x')