def return_binary_or_hexa(tup):
    a = tup[19]
    b = tup[32]
    integers_in_tup = tup[20:32]
    sum_integers = sum(range(a + 1, b))
    integers_not_in_tup = [i for i in range(a + 1, b) if i not in integers_in_tup]
    if not integers_not_in_tup:
        return ''
    sum_integers_not_in_tup = sum(integers_not_in_tup)
    if sum_integers_not_in_tup % 2 == 0:
        return hex(sum_integers_not_in_tup)[2:]
    else:
        return bin(sum_integers_not_in_tup)[2:]