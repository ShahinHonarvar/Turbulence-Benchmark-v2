def return_binary_or_hexa(arr):
    a = arr[73]
    b = arr[84]
    sum = 0
    for i in range(a + 1, b):
        if i not in arr[73:85]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()