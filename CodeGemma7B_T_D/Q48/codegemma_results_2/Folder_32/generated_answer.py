def return_binary_or_hexa(tu):
    a = tu[86]
    b = tu[90]
    real_tu = [e for i, e in enumerate(tu) if i not in range(86, 91)]
    sum = 0
    for i in range(a + 1, b):
        if not any((x == i for x in real_tu)):
            sum += i
    if sum % 2:
        return format(sum, 'b')
    return format(sum, 'x')