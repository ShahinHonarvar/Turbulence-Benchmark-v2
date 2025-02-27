def return_binary_or_hexa(t):
    a = t[0]
    b = t[5]
    existing_nums = set(t[:6])
    missing_sum = sum((x for x in range(a + 1, b) if x not in existing_nums))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')