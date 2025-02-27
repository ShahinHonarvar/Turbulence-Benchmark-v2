def return_binary_or_hexa(arr):
    a = arr[36]
    b = arr[54]
    present = set(arr[36:54])
    needed = set(range(a + 1, b))
    missing = needed.difference(present)
    sum_missing = sum(missing)
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]