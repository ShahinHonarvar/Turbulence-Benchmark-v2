def return_binary_or_hexa(t):
    a = t[10]
    b = t[76]
    excluded = set(t[10:77])
    sum_result = sum((i for i in range(a + 1, b) if i not in excluded))
    if sum_result == 0:
        return ''
    if sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:]