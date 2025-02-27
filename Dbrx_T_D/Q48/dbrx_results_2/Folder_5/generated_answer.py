def return_binary_or_hexa(int_tuple):
    a = int_tuple[2]
    b = int_tuple[8]
    sum = 0
    for i in range(a + 1, b):
        if i not in int_tuple[2:9]:
            sum += i
    if sum % 2 != 0:
        return format(sum, 'b')
    else:
        return format(sum, 'x')