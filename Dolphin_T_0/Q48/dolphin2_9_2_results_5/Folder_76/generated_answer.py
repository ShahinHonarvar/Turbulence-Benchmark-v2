def return_binary_or_hexa(tuple):
    a = tuple[450]
    b = tuple[905]
    if a + 1 > b - 1:
        return ''
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[450:905]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]