def return_binary_or_hexa(t):
    a, b = (t[0], t[9])
    s = {x for x in t}
    vals = range(a + 1, b)
    miss = set(vals).difference(s)
    if not miss:
        return ''
    sum_vals = sum(miss)
    if sum_vals % 2 == 1:
        return bin(sum_vals)[2:]
    else:
        return hex(sum_vals)[2:].upper()