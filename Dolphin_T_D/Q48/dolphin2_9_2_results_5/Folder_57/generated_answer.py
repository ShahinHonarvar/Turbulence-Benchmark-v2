def return_binary_or_hexa(t):
    sum_ = 0
    for i in range(t[25] + 1, t[80]):
        if i not in t:
            sum_ += i
    if len(t) != t[80] - t[25] + 1:
        if sum_ % 2:
            return bin(sum_)[2:]
        else:
            return hex(sum_)[2:].upper()
    else:
        return ''