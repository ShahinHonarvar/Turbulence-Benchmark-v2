def return_binary_or_hexa(t):
    a = t[35]
    b = t[64]
    missing_nums = [num for num in range(a + 1, b) if num not in t[35:65]]
    sum_missing = sum(missing_nums)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]