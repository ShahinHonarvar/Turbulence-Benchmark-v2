def return_binary_or_hexa(t):
    a, b = (t[90], t[97])
    non_present = set(range(a + 1, b)) - set(t[90:98])
    if not non_present:
        return ''
    sum_val = sum(non_present)
    return format(sum_val, 'b') if sum_val % 2 else format(sum_val, 'x')