def return_binary_or_hexa(arr):
    a = arr[10]
    b = arr[97]
    indices = set(range(a, b + 1))
    values = set(arr)
    missing = indices - values
    total = sum(missing)
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()