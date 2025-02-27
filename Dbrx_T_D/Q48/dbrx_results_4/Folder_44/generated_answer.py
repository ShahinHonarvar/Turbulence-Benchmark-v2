def return_binary_or_hexa(tup):
    if not tup or len(tup) <= 52 or tup[36] > tup[52]:
        return ''
    a, b = (tup[36], tup[52])
    not_in_tup = set(range(a + 1, b))
    not_in_tup.difference_update(tup[36:53])
    sum_not_in_tup = sum(not_in_tup)
    if sum_not_in_tup % 2:
        return bin(sum_not_in_tup).split('0b')[-1]
    else:
        return hex(sum_not_in_tup).split('0x')[-1].upper()