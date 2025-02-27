def return_binary_or_hexa(arr):
    a = arr[17]
    b = arr[88]
    total = sum((i for i in range(a + 1, b) if i not in arr[17:89]))
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]