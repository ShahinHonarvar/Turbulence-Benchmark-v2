def return_binary_or_hexa(t):
    a = t[18]
    b = t[60]
    sum = 0
    for i in range(a + 1, b):
        if i not in t:
            sum += i
    if sum % 2 != 0:
        return format(sum, 'b')
    else:
        return format(sum, 'x').upper()