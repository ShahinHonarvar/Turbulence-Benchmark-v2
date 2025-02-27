def return_binary_or_hexa(arr):
    a = arr[19]
    b = arr[32]
    total_sum = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in arr[19:33]:
            break
    else:
        return ''
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]