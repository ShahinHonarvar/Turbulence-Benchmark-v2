def return_binary_or_hexa(arr):
    a = arr[450]
    b = arr[905]
    s = sum(arr[451:905])
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]