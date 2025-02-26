def return_binary_or_hexa(arr):
    a = arr[1]
    b = arr[8]
    excluded = set(arr[1:9])
    sum_of_missing = sum((num for num in range(a + 1, b) if num not in excluded))
    if sum_of_missing == 0:
        return ''
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]