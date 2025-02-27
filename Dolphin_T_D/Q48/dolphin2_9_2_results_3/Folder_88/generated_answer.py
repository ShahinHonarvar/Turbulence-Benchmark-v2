def return_binary_or_hexa(arr):
    total = sum(arr[3:10])
    a = arr[3]
    b = arr[9]
    for i in range(a + 1, b):
        if i not in arr[3:10]:
            total += i
    if total % 2 == 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]