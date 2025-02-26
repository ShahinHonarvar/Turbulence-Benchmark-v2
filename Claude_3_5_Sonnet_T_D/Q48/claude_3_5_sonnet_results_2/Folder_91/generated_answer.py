def return_binary_or_hexa(t):
    a, b = (t[0], t[6])
    sum_not_present = sum(set(range(a + 1, b)) - set(t[:7]))
    if sum_not_present == 0:
        return ''
    if sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]