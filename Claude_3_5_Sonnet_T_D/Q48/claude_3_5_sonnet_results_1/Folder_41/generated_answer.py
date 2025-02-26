def return_binary_or_hexa(t):
    a = t[3]
    b = t[8]
    excluded = set(t[3:9])
    sum_range = sum((x for x in range(a + 1, b) if x not in excluded))
    if sum_range == 0:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:].rstrip('L')