def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    sum_range = sum((i for i in range(a + 1, b) if i not in t[2:8]))
    if sum_range == 0:
        return ''
    elif sum_range % 2 != 0:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:]