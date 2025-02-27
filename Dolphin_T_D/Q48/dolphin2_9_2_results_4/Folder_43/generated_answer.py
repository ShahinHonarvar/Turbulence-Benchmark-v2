def return_binary_or_hexa(arr):
    a = arr[10]
    b = arr[28]
    miss_vals = [x for x in range(a + 1, b) if x not in arr]
    if not miss_vals:
        return ''
    total = sum(miss_vals)
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()