def return_binary_or_hexa(t):
    a = t[3]
    b = t[8]
    middle_range = set(t[3:9])
    sum_not_present = sum((x for x in range(a + 1, b) if x not in middle_range))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].rstrip('L')