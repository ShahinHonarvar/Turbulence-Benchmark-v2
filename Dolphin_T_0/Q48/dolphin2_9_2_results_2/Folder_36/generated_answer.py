def return_binary_or_hexa(arr):
    a = arr[110]
    b = arr[348]
    missing_sum = sum((i for i in range(a + 1, b) if i not in arr))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]