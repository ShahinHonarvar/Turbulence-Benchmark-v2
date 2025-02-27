def return_binary_or_hexa(tuple1):
    a = tuple1[19]
    b = tuple1[32]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple1[19:33]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]