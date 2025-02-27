def return_binary_or_hexa(tuple_):
    a = tuple_[20]
    b = tuple_[43]
    if all((x in range(a + 1, b) for x in tuple_[20:44])):
        return ''
    else:
        x = sum((x for x in range(a + 1, b) if x not in tuple_[20:44]))
        output = bin(x) if x % 2 != 0 else hex(x)
        return output[2:].upper().lstrip('0')