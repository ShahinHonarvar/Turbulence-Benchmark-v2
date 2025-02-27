def return_binary_or_hexa(arr):
    a = arr[16]
    b = arr[87]
    if all((i in arr[17:87] for i in range(a + 1, b))):
        return ''
    else:
        missing = [i for i in range(a + 1, b) if i not in arr[17:87]]
        sum_missing = sum(missing)
        if sum_missing % 2 != 0:
            return bin(sum_missing)[2:]
        else:
            return hex(sum_missing)[2:]