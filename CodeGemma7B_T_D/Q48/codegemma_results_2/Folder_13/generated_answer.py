def return_binary_or_hexa(t):
    a, b = (t[46], t[91])
    sum = 0
    for i in range(a + 1, b):
        if i not in t[46:92]:
            sum += i
    sum_binary = format(sum, 'b')[2:]
    sum_hexa = format(sum, 'x')[2:]
    if sum % 2:
        return sum_binary
    return sum_hexa