def return_binary_or_hexa(arr):
    a = arr[29]
    b = arr[53]
    sum = 0
    for i in range(a + 1, b):
        if arr.index(i) < 29 or arr.index(i) > 53:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()