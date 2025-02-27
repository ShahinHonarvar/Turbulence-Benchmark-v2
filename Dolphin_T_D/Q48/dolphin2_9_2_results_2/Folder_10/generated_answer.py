def return_binary_or_hexa(tuples):
    a = tuples[36]
    b = tuples[54]
    indices = set(tuples[37:54])
    total = sum((i for i in range(a + 1, b) if i not in indices))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()