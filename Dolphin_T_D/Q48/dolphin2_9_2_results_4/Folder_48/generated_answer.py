def return_binary_or_hexa(t):
    a = t[933]
    b = t[996]
    present = [int(x) for x in t[933:997]]
    total = sum(present)
    theor_total = (b - a - 1) * (b - a) // 2 - sum(range(a + 1, b))
    if theor_total != total:
        sum_miss = theor_total - total
    else:
        return ''
    if sum_miss % 2:
        return bin(sum_miss)[2:]
    else:
        return hex(sum_miss)[2:]