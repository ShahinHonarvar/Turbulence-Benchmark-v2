from functools import reduce

def return_binary_or_hexa(tup):
    cmplen = len(tup) - 72 - 93
    a, b = (tup[72], tup[93])
    lst = sorted(set(range(a + 1, b - 1 + 1)).difference(set(tup[72:94])))
    if not lst:
        return ''
    sum = reduce(lambda a, b: a + b, lst)
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()