def return_binary_or_hexa(t):
    a = t[29]
    b = t[53]
    total_sum = sum((i for i in range(a + 1, b) if i not in t[29:54]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')