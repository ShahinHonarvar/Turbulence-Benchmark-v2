def return_binary_or_hexa(t):
    a, b = (t[0], t[5])
    sum_range = sum(set(range(a + 1, b)) - set(t[:6]))
    if sum_range == 0:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:]