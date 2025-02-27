def return_binary_or_hexa(arr):
    a = arr[10]
    b = arr[97]
    total = sum((val for val in range(a + 1, b) if val not in arr))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()