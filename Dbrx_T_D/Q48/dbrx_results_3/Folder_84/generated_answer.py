def return_binary_or_hexa(arr):
    a, b = (arr[32], arr[44])
    if a >= b:
        return ''
    missing_sum = sum((x for x in range(a + 1, b) if arr[32:45].count(x) == 0))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()