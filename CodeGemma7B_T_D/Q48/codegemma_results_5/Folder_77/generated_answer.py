def return_binary_or_hexa(arr):
    a, b = (arr[18], arr[52])
    sum = 0
    for i in range(a + 1, b):
        if i not in arr[18:53]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()