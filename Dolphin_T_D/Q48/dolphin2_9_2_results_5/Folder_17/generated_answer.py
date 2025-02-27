def return_binary_or_hexa(array):
    a = array[73]
    b = array[84]
    sum = 0
    for i in range(a + 1, b):
        if i not in array[73:84 + 1]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]