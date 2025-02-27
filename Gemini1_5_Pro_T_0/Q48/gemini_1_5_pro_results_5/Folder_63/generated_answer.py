def return_binary_or_hexa(tuple1):
    a = tuple1[81]
    b = tuple1[86]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple1[81:87]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]