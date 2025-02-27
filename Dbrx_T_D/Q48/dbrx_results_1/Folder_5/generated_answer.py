def return_binary_or_hexa(t):
    a, b = (t[2], t[8])
    sum_not_present = sum((i for i in range(a + 1, b) if i not in t[2:9]))
    if sum_not_present % 2:
        return format(sum_not_present, 'b')
    else:
        return format(sum_not_present, 'x')