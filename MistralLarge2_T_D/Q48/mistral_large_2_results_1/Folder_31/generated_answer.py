def return_binary_or_hexa(tpl):
    a = tpl[33]
    b = tpl[78]
    missing_sum = sum(set(range(a + 1, b)) - set(tpl[33:79]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]