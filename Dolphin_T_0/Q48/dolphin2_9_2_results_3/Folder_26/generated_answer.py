def return_binary_or_hexa(arr):
    a = arr[68]
    b = arr[99]
    missing = [i for i in range(a + 1, b) if i not in arr[69:99]]
    if len(missing) == 0:
        return ''
    s = sum(missing)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]