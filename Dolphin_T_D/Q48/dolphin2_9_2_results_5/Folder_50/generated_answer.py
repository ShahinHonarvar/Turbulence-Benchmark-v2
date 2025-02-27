def return_binary_or_hexa(t):
    a = t[13]
    b = t[76]
    present = [x for x in t[14:76]]
    if all((x in present for x in range(a + 1, b))):
        return ''
    sum_ = 0
    for x in range(a + 1, b):
        if x not in present:
            sum_ += x
    return bin(sum_)[2:] if sum_ % 2 else hex(sum_)[2:]