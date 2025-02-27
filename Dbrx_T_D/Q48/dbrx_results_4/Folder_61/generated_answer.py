def return_binary_or_hexa(t):
    a, b = (t[0], t[8])
    s = set(t[1:8])
    sum = 0
    for i in range(a + 1, b):
        if i not in s:
            sum += i
    if sum % 2:
        return format(sum, 'b')
    else:
        return format(sum, 'x')