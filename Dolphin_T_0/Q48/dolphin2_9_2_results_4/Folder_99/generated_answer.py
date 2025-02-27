def return_binary_or_hexa(arr):
    a = arr[427]
    b = arr[669]
    if len(arr[arr.index(a) + 1:arr.index(b)]) == b - a - 1:
        return ''
    sum = 0
    for i in range(a + 1, b):
        if i not in arr[arr.index(a) + 1:arr.index(b)]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]