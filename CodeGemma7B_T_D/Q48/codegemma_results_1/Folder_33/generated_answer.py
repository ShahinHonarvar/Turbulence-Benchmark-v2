from functools import reduce

def return_binary_or_hexa(tup):
    a, b = (tup[13], tup[35])
    total = reduce(lambda x, y: x + y, range(a + 1, b))
    sum_set = set(tup[13:36])
    final = total - sum(sum_set)
    if final % 2 == 1:
        return bin(final)[2:]
    elif final % 16 == 0:
        return hex(final)[2:].upper()
    else:
        return hex(final)[2:]