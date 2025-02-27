def return_binary_or_hexa(t):
    a = t[38]
    b = t[81]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in t[38:81]:
            sum_ += i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    elif sum_ == 0:
        return ''
    else:
        return hex(sum_)[2:]