def return_binary_or_hexa(arr):
    a = arr[90]
    b = arr[97]
    total = sum(range(a + 1, b)) - sum(arr[90:98])
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()