def return_binary_or_hexa(arr):
    a = arr[35]
    b = arr[64]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in arr[36:65]:
            missing_sum += i
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]