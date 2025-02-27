def return_binary_or_hexa(arr):
    a = arr[37]
    b = arr[43]
    summ = 0
    for i in range(a + 1, b):
        if i not in arr:
            summ += i
    if summ % 2 == 0:
        return hex(summ)[2:]
    return bin(summ)[2:]