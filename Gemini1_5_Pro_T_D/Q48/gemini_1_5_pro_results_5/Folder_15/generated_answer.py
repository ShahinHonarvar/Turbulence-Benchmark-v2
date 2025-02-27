def return_binary_or_hexa(tpl):
    sum = 0
    for i in range(tpl[0] + 1, tpl[4]):
        if i not in tpl:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    return hex(sum)[2:]