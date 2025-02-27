def return_binary_or_hexa(t):
    a, b = (t[77], t[84])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[77:85]))
    if missing_sum % 2:
        return '{:b}'.format(missing_sum)
    else:
        return '{:x}'.format(missing_sum).upper()