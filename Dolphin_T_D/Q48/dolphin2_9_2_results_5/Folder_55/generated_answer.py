def return_binary_or_hexa(integers_tuple):
    a = integers_tuple[10]
    b = integers_tuple[12]
    sum = 0
    for i in range(a + 1, b):
        if i not in integers_tuple[10:13]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]