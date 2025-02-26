def return_binary_or_hexa(t):
    a, b = (t[0], t[3])
    sum_range = set(range(a + 1, b))
    sum_tuple = set(t[1:3])
    sum_diff = sum(sum_range - sum_tuple)
    if sum_diff == 0:
        return ''
    elif sum_diff % 2 == 1:
        return bin(sum_diff)[2:]
    else:
        return hex(sum_diff)[2:]