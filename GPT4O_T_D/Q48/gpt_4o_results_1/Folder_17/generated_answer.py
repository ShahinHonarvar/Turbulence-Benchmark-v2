def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    sum_value = 0
    for i in range(a + 1, b):
        if i not in t[74:84]:
            sum_value += i
    if sum_value == 0:
        return ''
    if sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]