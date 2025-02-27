def return_binary_or_hexa(arr):
    a = arr[57]
    b = arr[85]
    missing = [x for x in range(a + 1, b) if x not in arr]
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]