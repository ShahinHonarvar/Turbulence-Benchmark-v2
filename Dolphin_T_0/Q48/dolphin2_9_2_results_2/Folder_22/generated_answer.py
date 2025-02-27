def return_binary_or_hexa(arr):
    a = arr[40]
    b = arr[200]
    existing = [num for num in range(a + 1, b) if num in arr[41:200]]
    missing = [num for num in range(a + 1, b) if num not in existing]
    sum_missing = sum(missing)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]