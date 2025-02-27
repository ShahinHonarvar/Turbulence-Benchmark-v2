def return_binary_or_hexa(t):
    a = t[80]
    b = t[200]
    sum_nums = sum(range(a + 1, b)) - sum(t[81:200])
    if all((i in t[81:200] for i in range(a + 1, b))):
        return ''
    elif sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]