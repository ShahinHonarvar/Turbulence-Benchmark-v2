def return_binary_or_hexa(arr):
    a = arr[69]
    b = arr[97]
    missing = [i for i in range(a + 1, b) if i not in arr[70:97]]
    if not missing:
        return ''
    s = sum(missing)
    return bin(s)[2:] if s % 2 == 1 else hex(s)[2:]