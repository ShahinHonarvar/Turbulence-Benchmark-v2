def return_binary_or_hexa(tuple_):
    a = tuple_[13]
    b = tuple_[91]
    total = 0
    for i in range(a + 1, b):
        if i not in tuple_[13:92]:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]