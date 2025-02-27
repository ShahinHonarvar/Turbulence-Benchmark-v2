def return_binary_or_hexa(arr):
    a = arr[57]
    b = arr[84]
    sum = 0
    for i in range(a + 1, b):
        if i not in arr[57:85]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    elif sum != 0:
        return hex(sum)[2:].upper()
    else:
        return ''