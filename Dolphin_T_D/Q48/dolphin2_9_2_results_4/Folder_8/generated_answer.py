def return_binary_or_hexa(arr):
    a = arr[45]
    b = arr[48]
    missing = [x for x in range(a + 1, b) if x not in arr[45:49]]
    if not missing:
        return ''
    s = sum(missing)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].lower()