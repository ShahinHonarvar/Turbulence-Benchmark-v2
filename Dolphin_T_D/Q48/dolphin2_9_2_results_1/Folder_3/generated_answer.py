def return_binary_or_hexa(arr):
    a, b = (arr[56], arr[88])
    missing = [x for x in range(a + 1, b) if x not in arr[56:88 + 1]]
    if missing:
        s = sum(missing)
        if s % 2 == 0:
            return hex(s)[2:]
        else:
            return bin(s)[2:]
    else:
        return ''