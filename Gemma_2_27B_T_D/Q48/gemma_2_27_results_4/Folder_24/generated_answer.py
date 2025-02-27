def return_binary_or_hexa(tpl):
    a = tpl[13]
    b = tpl[91]
    total = sum((x for x in range(a + 1, b) if x not in tpl[13:92]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()