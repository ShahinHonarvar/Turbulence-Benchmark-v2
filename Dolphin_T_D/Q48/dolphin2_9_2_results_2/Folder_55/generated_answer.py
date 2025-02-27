def return_binary_or_hexa(arr):
    a, b = (arr[10], arr[12])
    total = sum((i for i in range(a + 1, b) if i not in arr[11:12]))
    if total % 2 != 0:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:].upper()
    return ''