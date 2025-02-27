def return_binary_or_hexa(tuples):
    a = tuples[20]
    b = tuples[93]
    tup = tuples[20:94]
    total = range(a + 1, b)
    missing = [i for i in total if i not in tup]
    summ = sum(missing)
    if summ % 2 == 0:
        result = hex(summ)[2:].upper()
    else:
        result = bin(summ)[2:]
    if not missing:
        return ''
    return result