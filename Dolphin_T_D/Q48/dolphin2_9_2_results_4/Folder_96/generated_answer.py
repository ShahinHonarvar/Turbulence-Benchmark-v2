def return_binary_or_hexa(arr):
    a = arr[50]
    b = arr[200]
    missing = [i for i in range(a + 1, b) if i not in arr[50:200]]
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return str(bin(sum_missing))[2:]
    else:
        return hex(sum_missing)[2:]