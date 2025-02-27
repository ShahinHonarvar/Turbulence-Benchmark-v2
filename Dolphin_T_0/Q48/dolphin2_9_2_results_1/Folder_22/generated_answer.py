def return_binary_or_hexa(arr):
    a = arr[40]
    b = arr[200]
    if all((i in arr[40:201] for i in range(a + 1, b))):
        return ''
    sum = 0
    for i in range(a + 1, b):
        if i not in arr[41:201] and i != a and (i != b - 1):
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper() if sum != 0 else '0'