def return_binary_or_hexa(input_tuple):
    a = input_tuple[48]
    b = input_tuple[76]
    sum = 0
    for i in range(a + 1, b):
        if i not in input_tuple[48:76]:
            sum += i
    if sum % 2 == 1:
        return '{0:08b}'.format(sum)
    else:
        return '{:02x}'.format(sum).upper()