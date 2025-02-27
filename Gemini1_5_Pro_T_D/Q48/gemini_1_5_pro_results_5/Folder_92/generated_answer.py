def return_binary_or_hexa(tpl):
    a = tpl[0]
    b = tpl[2]
    sum = 0
    for i in range(a + 1, b):
        if i not in tpl:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]