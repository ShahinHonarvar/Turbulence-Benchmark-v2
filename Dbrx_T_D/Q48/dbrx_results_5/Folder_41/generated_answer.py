def return_binary_or_hexa(t):
    a, b = (t[3], t[8])
    sum_of_absent = sum((x for x in range(a + 1, b) if x not in t[3:8]))
    if sum_of_absent % 2:
        return format(sum_of_absent, 'b')
    else:
        return format(sum_of_absent, 'x').upper()