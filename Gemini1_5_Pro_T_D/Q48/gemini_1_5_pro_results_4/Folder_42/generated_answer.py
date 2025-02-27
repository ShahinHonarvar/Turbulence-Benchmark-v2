def return_binary_or_hexa(tpl):
    a = tpl[18]
    b = tpl[60]
    sum = 0
    for i in range(a + 1, b):
        if i not in tpl[18:61]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()