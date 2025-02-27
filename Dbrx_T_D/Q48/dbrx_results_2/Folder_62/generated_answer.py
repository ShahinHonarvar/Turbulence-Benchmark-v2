def return_binary_or_hexa(t):
    a, b = (t[50], t[92])
    missing_sum = sum((i for i in range(a + 1, b) if t[50:93].count(i) == 0))
    if missing_sum % 2:
        return format(missing_sum, '08b')
    else:
        return format(missing_sum, 'x').upper()