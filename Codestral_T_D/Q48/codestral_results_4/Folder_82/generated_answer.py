def return_binary_or_hexa(tuples):
    a = tuples[20]
    b = tuples[200]
    missing_numbers = set(range(a + 1, b)) - set(tuples[20:200])
    sum_missing = sum(missing_numbers)
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:]