def return_binary_or_hexa(arr):
    a, b = (arr[68], arr[99])
    missing = [i for i in range(a + 1, b) if i not in arr]
    if not missing:
        return ''
    s = sum(missing)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]