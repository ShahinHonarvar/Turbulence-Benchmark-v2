def return_binary_or_hexa(arr):
    a, b = (arr[37], arr[43])
    sum = 0
    for i in range(a + 1, b):
        if i not in arr[37:43]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()