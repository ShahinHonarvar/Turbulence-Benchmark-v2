def return_binary_or_hexa(t):
    if len(t) != 7:
        return ''
    a = t[2]
    b = t[5]
    present = [i for i in t if i >= a and i <= b]
    values = list(range(a + 1, b))
    not_present = [i for i in values if i not in present]
    sum_ = sum(not_present)
    return bin(sum_)[2:] if sum_ % 2 != 0 else hex(sum_)[2:]