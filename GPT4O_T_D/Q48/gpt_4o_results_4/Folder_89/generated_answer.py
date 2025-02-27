def return_binary_or_hexa(t):
    a = t[55]
    b = t[84]
    existing_set = set(t[56:84])
    all_nums_sum = sum((n for n in range(a + 1, b) if n not in existing_set))
    if all_nums_sum == 0:
        return ''
    if all_nums_sum % 2 == 0:
        return format(all_nums_sum, 'x')
    else:
        return format(all_nums_sum, 'b')