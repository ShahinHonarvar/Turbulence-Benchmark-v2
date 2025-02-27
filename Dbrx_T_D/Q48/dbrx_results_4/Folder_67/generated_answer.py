def return_binary_or_hexa(t):
    a, b = (t[44], t[67])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[44:68]))
    if missing_sum % 2:
        return format(missing_sum, '08b')
    else:
        return format(missing_sum, 'x').upper()