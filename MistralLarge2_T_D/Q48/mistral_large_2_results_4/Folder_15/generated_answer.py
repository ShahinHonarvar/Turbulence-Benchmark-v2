def return_binary_or_hexa(t):
    a, b = (t[0], t[4])
    sum_ = sum((x for x in range(a + 1, b) if x not in t[:5]))
    if sum_ == 0:
        return ''
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()