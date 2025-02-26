def return_binary_or_hexa(t):
    a = t[19]
    b = t[32]
    excluded = set(t[19:33])
    sum_range = sum((i for i in range(a + 1, b) if i not in excluded))
    if sum_range == 0:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:].rstrip('L')