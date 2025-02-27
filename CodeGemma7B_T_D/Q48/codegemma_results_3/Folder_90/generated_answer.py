def return_binary_or_hexa(t):
    a = t[60]
    b = t[90]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[60:91]:
            sum += i
    if sum % 2:
        return format(sum, 'b')[2:]
    else:
        return format(sum, 'x')[2:]