def return_binary_or_hexa(arr):
    a = arr[0]
    b = arr[8]
    s = sum((x for x in range(a + 1, b) if x not in arr))
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]