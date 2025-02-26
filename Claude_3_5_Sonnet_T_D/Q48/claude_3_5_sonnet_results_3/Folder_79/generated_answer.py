def return_binary_or_hexa(t):
    a, b = (t[1], t[7])
    sum_not_present = sum(set(range(a + 1, b)) - set(t[1:8]))
    if sum_not_present == 0:
        return ''
    if sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()