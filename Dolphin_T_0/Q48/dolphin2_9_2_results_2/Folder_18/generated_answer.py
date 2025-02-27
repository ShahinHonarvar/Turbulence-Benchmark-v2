def return_binary_or_hexa(arr):
    total = 0
    present = set(arr[57:91])
    for i in range(arr[56] + 1, arr[90]):
        if i not in present:
            total += i
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]