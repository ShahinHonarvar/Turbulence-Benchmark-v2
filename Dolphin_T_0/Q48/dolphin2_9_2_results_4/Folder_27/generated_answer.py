def return_binary_or_hexa(arr):
    a = arr[86]
    b = arr[89]
    if sum((x for x in range(a + 1, b) if x not in arr)) == 0:
        return ''
    summ = sum((x for x in range(a + 1, b) if x not in arr))
    if summ % 2 == 0:
        return bin(summ)[2:]
    else:
        return hex(summ)[2:].upper()