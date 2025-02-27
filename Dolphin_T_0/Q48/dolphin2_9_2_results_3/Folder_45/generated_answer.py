def return_binary_or_hexa(arr):
    a = arr[30]
    b = arr[200]
    sum = 0
    for i in range(a + 1, b):
        sum += 1 if i not in arr[30:200] else 0
    if sum % 2 == 1:
        return bin(sum)[2:]
    elif sum != 0:
        return hex(sum)[2:]
    else:
        return ''