def return_binary_or_hexa(t):
    a, b = (t[0], t[2])
    sum_not_present = sum(set(range(a + 1, b)) - set(t[0:3]))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]