def return_binary_or_hexa(tuples):
    a = tuples[68]
    b = tuples[99]
    missing_nums = [i for i in range(a + 1, b) if i not in tuples[68:99]]
    sum_missing = sum(missing_nums)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]