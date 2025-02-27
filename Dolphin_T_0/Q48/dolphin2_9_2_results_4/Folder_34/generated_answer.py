def return_binary_or_hexa(arr):
    a = arr[60]
    b = arr[200]
    missing = [i for i in range(a + 1, b) if i not in arr[60:201]]
    summ = sum(missing)
    if summ % 2:
        return bin(summ)[2:]
    else:
        return hex(summ)[2:]