def return_binary_or_hexa(num_tuple):
    a = num_tuple[39]
    b = num_tuple[43]
    if a + 1 > b - 1:
        return ''
    sum = 0
    for i in range(a + 1, b):
        if i not in num_tuple[39:44]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()