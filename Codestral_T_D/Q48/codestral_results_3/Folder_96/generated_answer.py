def return_binary_or_hexa(t):
    a = t[50]
    b = t[200]
    subset = set(t[51:200])
    missing_nums = [num for num in range(a + 1, b) if num not in subset]
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''