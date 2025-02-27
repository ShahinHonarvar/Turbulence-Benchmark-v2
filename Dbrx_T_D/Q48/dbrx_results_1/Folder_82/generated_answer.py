def return_binary_or_hexa(t):
    a, b = (t[20], t[200])
    sum_missing = sum((i for i in range(a + 1, b) if i not in t[20:201]))
    if sum_missing % 2:
        return format(sum_missing, '08b')
    else:
        return format(sum_missing, 'x').upper()