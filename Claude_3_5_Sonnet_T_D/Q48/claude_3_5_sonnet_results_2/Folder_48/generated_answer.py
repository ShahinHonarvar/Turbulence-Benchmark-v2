def return_binary_or_hexa(t):
    a = t[933]
    b = t[996]
    sum_not_present = sum(set(range(a + 1, b)) - set(t[933:997]))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]