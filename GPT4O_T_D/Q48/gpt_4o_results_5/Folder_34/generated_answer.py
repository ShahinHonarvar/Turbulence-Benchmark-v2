def return_binary_or_hexa(tpl):
    a = tpl[60]
    b = tpl[200]
    missing_sum = sum((x for x in range(a + 1, b) if x not in tpl[61:200]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return f'{missing_sum:b}'
    else:
        return f'{missing_sum:x}'