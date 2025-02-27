def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    sum_missing = 0
    for i in range(a + 1, b):
        if i not in t[73:85]:
            sum_missing += i
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]