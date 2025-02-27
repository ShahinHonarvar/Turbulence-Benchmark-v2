def return_binary_or_hexa(tpl):
    a = tpl[86]
    b = tpl[89]
    total = 0
    for i in range(a + 1, b):
        if i not in tpl[86:89 + 1]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]