def return_binary_or_hexa(arr):
    a = arr[68]
    b = arr[99]
    sum = 0
    for i in range(a + 1, b):
        if i not in arr[68:100]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()