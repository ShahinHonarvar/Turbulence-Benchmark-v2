def return_binary_or_hexa(t):
    a, b = (t[0], t[3])
    excluded = set(t[1:3])
    sum_range = sum((i for i in range(a + 1, b) if i not in excluded))
    if sum_range == 0:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:]