def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[51]
    sum_all = b - a - 1
    if sum_all < 0:
        return ''
    refer_sum = sum(range(a + 1, b)) - sum(tup[21:51])
    if refer_sum == sum_all:
        return ''
    if refer_sum % 2 == 0:
        return hex(refer_sum)[2:]
    else:
        return bin(refer_sum)[2:]