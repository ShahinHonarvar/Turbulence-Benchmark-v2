def return_binary_or_hexa(t):
    a, b = (t[35], t[64])
    sum_not_in_range = sum(set(range(a + 1, b)) - set(t[35:65]))
    if sum_not_in_range % 2:
        return bin(sum_not_in_range)[2:]
    else:
        return hex(sum_not_in_range)[2:].upper()