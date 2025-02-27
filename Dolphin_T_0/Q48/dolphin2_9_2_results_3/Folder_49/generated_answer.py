def return_binary_or_hexa(t):
    a = t[80]
    b = t[200]
    if a > b:
        return ''
    sum_ = 0
    for num in range(a + 1, b):
        if num not in t:
            sum_ += num
    if sum_ % 2:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()