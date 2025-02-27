def return_binary_or_hexa(tuples):
    a = tuples[60]
    b = tuples[90]
    missing = sum(range(a + 1, b)) - sum(tuples[60:91])
    if missing > 0:
        if missing % 2 == 1:
            return bin(missing)[2:]
        else:
            return hex(missing)[2:].upper()
    else:
        return ''