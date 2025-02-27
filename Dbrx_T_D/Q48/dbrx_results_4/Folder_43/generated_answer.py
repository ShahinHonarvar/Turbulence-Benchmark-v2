def return_binary_or_hexa(tpl):
    a, b = (tpl[10], tpl[28])
    sum = 0
    for i in range(a + 1, b):
        if i not in tpl:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()