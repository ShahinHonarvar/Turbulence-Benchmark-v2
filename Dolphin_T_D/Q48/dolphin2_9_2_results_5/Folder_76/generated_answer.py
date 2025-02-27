def return_binary_or_hexa(arr):
    a = arr[450]
    b = arr[905]
    missing = []
    for i in range(a + 1, b):
        if i not in arr:
            missing.append(i)
    sum = 0
    for i in missing:
        sum += i
    if sum % 2 != 0:
        return bin(sum).replace('0b', '')
    else:
        return hex(sum).replace('0x', '')