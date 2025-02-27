def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[20]
    b = numbers_tuple[35]
    sum_ = sum(set(range(a + 1, b)) - set(numbers_tuple[20:36]))
    if not sum_:
        return ''
    elif sum_ % 2:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]