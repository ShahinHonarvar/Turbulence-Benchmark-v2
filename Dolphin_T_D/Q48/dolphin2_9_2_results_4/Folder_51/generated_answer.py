def return_binary_or_hexa(arr):
    a, b = (arr[6], arr[9])
    missing = [i for i in range(a + 1, b) if i not in arr]
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]