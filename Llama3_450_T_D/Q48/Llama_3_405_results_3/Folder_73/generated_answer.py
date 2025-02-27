def return_binary_or_hexa(t):
    a, b = (t[10], t[76])
    full_set = set(range(a + 1, b))
    actual_set = set(t[11:76])
    diff_set = full_set - actual_set
    s = sum(diff_set)
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]