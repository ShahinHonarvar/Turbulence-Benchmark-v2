def return_binary_or_hexa(t):
    a = t[36]
    b = t[52]
    present = set(t[36:53])
    sum_not_present = sum((i for i in range(a + 1, b) if i not in present))
    if sum_not_present == 0:
        return ''
    if sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]