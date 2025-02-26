def return_binary_or_hexa(t):
    a, b = (t[0], t[3])
    excluded = set(t[0:4])
    sum_excluded = sum((i for i in range(a + 1, b) if i not in excluded))
    if sum_excluded == 0:
        return ''
    elif sum_excluded % 2 == 1:
        return bin(sum_excluded)[2:]
    else:
        return hex(sum_excluded)[2:]