def return_binary_or_hexa(lst):
    a, b = (lst[35], lst[64])
    missing = [i for i in range(a + 1, b) if i not in lst]
    sum_missing = sum(missing)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missig)[2:].upper()