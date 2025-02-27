def return_binary_or_hexa(ints_tuple):
    a = ints_tuple[60]
    b = ints_tuple[200]
    sum = 0
    for i in range(a + 1, b):
        if ints_tuple.count(i) == 0:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]