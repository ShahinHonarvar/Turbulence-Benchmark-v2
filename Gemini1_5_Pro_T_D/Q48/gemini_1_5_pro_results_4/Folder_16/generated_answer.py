def return_binary_or_hexa(tuple1):
    a = tuple1[90]
    b = tuple1[97]
    sum1 = 0
    for i in range(a + 1, b):
        if i not in tuple1[90:98]:
            sum1 += i
    if sum1 == 0:
        return ''
    elif sum1 % 2 == 1:
        return bin(sum1)[2:]
    else:
        return hex(sum1)[2:]