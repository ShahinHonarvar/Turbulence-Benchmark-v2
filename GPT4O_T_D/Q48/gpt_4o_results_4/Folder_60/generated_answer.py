def return_binary_or_hexa(t):
    a = t[38]
    b = t[52]
    total_sum = sum((x for x in range(a + 1, b) if x not in t[39:52]))
    if total_sum == 0:
        return ''
    return f'{total_sum:b}' if total_sum % 2 else f'{total_sum:X}'