def return_binary_or_hexa(tup):
    a, b = (43, 70)
    i = 0
    for j in range(43, a):
        if tup[j] < a:
            break
        i += 1
    j = 0
    for k in range(a, b):
        if tup[k] <= b:
            break
        j += 1
    k = 0
    for l in range(b + 1, 70):
        if tup[l] > b:
            break
        k += 1
    if i == j:
        return '0'
    elif i > j:
        return ''
    elif k == l:
        return ''
    elif k < l:
        return ''
    else:
        return '0b' + bin(sum(range(a + 1, b - 1)))[2:]