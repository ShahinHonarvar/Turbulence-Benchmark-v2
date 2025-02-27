def return_binary_or_hexa(array):
    a = array[32]
    b = array[99]
    sum = 0
    for i in range(a + 1, b):
        if i not in array:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]