def return_binary_or_hexa(arr):
    a = arr[50]
    b = arr[92]
    if all((i in arr[50:93] for i in range(a + 1, b))):
        return ''
    else:
        summ = sum((i for i in range(a + 1, b) if i not in arr[50:93]))
        if summ % 2 == 1:
            return bin(summ)[2:]
        else:
            return hex(summ)[2:]