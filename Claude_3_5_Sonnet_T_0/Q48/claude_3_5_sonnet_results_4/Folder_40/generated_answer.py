def return_binary_or_hexa(t):
    a, b = (t[0], t[3])
    sum_range = sum(set(range(a + 1, b)) - set(t[:4]))
    if sum_range == 0:
        return ''
    if sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:]