def return_binary_or_hexa(tpl):
    a = tpl[1] + 1
    b = tpl[8] - 1
    if all((i in tpl for i in range(a, b + 1))):
        return ''
    sum = 0
    for i in range(a, b + 1):
        if i not in tpl:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()