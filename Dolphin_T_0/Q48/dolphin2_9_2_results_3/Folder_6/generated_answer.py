def return_binary_or_hexa(arr):
    a = arr[20]
    b = arr[93]
    if a + 1 > b - 1:
        return ''
    summ = 0
    for i in range(a + 1, b):
        if not a <= i <= b:
            summ += i
            if summ % 2 != 0:
                return bin(summ)[2:]
            else:
                return hex(summ)[2:].upper()
    return ''