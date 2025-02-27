def return_binary_or_hexa(tpl):
    a = tpl[3]
    b = tpl[9]
    s = sum((x for x in range(a + 1, b) if x not in tpl))
    if not s:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]