def return_binary_or_hexa(t):
    a, b = (t[0], t[9])
    sum_range = set(range(a + 1, b))
    sum_tuple = set(t[1:9])
    missing_sum = sum(sum_range - sum_tuple)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')