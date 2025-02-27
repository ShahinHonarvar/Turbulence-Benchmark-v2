def return_binary_or_hexa(arr):
    a = arr[46]
    b = arr[91]
    integers = arr[47:91]
    sum = 0
    for i in range(a + 1, b):
        if i not in integers:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]