def return_binary_or_hexa(t):
    a, b = (t[18], t[60])
    sum_of_missing = sum(set(range(a + 1, b)) - set(t[18:60]))
    if sum_of_missing % 2 != 0:
        return format(sum_of_missing, 'b')
    else:
        return hex(sum_of_missing)[2:].upper()