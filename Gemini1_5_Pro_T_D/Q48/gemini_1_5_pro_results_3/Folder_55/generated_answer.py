def return_binary_or_hexa(tuple_):
    a = tuple_[10]
    b = tuple_[12]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_[10:12]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]