def return_binary_or_hexa(t):
    a = t[3]
    b = t[9]
    sum_range = sum(set(range(a + 1, b)) - set(t[3:10]))
    if sum_range == 0:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:]