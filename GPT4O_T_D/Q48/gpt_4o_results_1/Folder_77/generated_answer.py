def return_binary_or_hexa(t):
    a = t[18]
    b = t[52]
    sum_missing = 0
    for num in range(a + 1, b):
        if num not in t[19:52]:
            sum_missing += num
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]