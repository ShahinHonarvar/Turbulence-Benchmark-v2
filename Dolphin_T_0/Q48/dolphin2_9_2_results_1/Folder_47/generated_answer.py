def return_binary_or_hexa(arr):
    a = arr[29]
    b = arr[53]
    present = arr[30:53]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in present:
            total_sum += i
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]