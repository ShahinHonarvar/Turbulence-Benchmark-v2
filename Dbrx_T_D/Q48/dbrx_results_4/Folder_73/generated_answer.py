def return_binary_or_hexa(arr):
    a = arr[10]
    b = arr[76]
    sum = 0
    for i in range(a + 1, b):
        if i not in arr[10:77]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()