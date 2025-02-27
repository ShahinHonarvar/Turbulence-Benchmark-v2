def return_binary_or_hexa(arr):
    a = arr[18]
    b = arr[60]
    sum = 0
    for i in range(a + 1, b):
        if i not in arr[19:60]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]