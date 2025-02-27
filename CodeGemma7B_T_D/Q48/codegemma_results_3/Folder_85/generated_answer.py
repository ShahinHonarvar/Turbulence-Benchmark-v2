def return_binary_or_hexa(a_b):
    a, b = (min(a_b), max(a_b))
    missing_nums = set(range(a + 1, b)) - set(a_b[1:9])
    sum_of_missing = sum(missing_nums)
    if sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:].upper()
    else:
        return bin(sum_of_missing)[2:]