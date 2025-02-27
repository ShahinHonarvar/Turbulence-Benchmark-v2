def return_binary_or_hexa(arr):
    a = arr[48]
    b = arr[76]
    missing_nums = set(range(a + 1, b)) - set(arr[48:76])
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total > 0:
        return hex(total)[2:]
    else:
        return ''