def return_binary_or_hexa(arr):
    a = arr[3]
    b = arr[8]
    missing = [x for x in range(a + 1, b) if x not in arr[3:9]]
    if not missing:
        return ''
    s = sum(missing)
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]