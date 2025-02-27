def return_binary_or_hexa(t):
    a = t[18]
    b = t[52]
    all_numbers = set(range(a + 1, b))
    t_set = set(t[19:53])
    diff_set = all_numbers.difference(t_set)
    if not diff_set:
        return ''
    sum_diff = sum(diff_set)
    if sum_diff % 2:
        return bin(sum_diff)[2:]
    else:
        return hex(sum_diff)[2:]