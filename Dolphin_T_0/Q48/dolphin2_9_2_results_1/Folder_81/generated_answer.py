def return_binary_or_hexa(lst):
    a, b = (lst[10], lst[100])
    present = set(lst[10:100])
    res = []
    for i in range(a + 1, b + 1):
        if i not in present:
            res.append(i)
    s = sum(res)
    if s == 0:
        return ''
    elif s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]