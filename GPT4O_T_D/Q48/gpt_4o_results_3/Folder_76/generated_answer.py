def return_binary_or_hexa(tpl):
    a = tpl[450]
    b = tpl[905]
    missing_sum = sum(set(range(a + 1, b)) - set(tpl[451:905]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return format(missing_sum, 'x').lstrip('0') or '0'
    else:
        return format(missing_sum, 'b').lstrip('0') or '0'