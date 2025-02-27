def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[70]
    missing_numbers = [i for i in range(a + 1, b) if i not in tup[13:70]]
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''