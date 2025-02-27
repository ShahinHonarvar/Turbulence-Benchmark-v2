def return_binary_or_hexa(arr):
    a = arr[32]
    b = arr[99]
    present_set = set(arr[33:99])
    sum = 0
    for i in range(a + 1, b):
        if i not in present_set:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()