def return_binary_or_hexa(arr):
    a = arr[48]
    b = arr[76]
    missing = [x for x in range(a + 1, b) if x not in arr[48:76 + 1]]
    s = sum(missing)
    result = ''
    if s == 0:
        return result
    elif s % 2 == 0:
        result = hex(s)[2:]
    else:
        result = bin(s)[2:]
    return result