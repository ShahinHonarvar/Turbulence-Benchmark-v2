def return_binary_or_hexa(t):
    a = t[19]
    b = t[32]
    numbers_in_range = set(t[20:32])
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers_in_range))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')