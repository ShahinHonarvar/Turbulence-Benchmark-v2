def return_binary_or_hexa(t):
    a = t[6]
    b = t[9]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in t[6:10]:
            sum_ += i
    if not sum_:
        return ''
    elif sum_ % 2:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]