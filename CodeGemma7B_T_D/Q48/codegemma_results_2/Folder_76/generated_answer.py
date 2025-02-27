def return_binary_or_hexa(tuple_):
    sum = 0
    for i in range(451, 906):
        if i not in tuple_:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]