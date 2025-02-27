def return_binary_or_hexa(tpl):
    a = tpl[38]
    b = tpl[81]
    sum = 0
    for i in range(a + 1, b):
        if i not in tpl[39:81]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]