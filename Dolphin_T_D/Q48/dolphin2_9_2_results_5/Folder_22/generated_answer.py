def return_binary_or_hexa(t):
    a = t[40]
    b = t[200]
    present = {i: 1 for i in range(a + 1, b)}
    for i in t[40:201]:
        if i in present:
            del present[i]
    if not present:
        return ''
    sum_ = sum(present.keys())
    if sum_ % 2 != 0:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]