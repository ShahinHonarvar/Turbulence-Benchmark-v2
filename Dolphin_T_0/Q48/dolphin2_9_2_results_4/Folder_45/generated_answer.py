def return_binary_or_hexa(tuples):
    a = tuples[30]
    b = tuples[200]
    present = set(tuples[31:200])
    result = sum(set(range(a + 1, b)) - present)
    if result % 2:
        return bin(result)[2:]
    else:
        return hex(result)[2:].upper()