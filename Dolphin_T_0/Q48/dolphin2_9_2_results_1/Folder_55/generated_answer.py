def return_binary_or_hexa(lst):
    a = lst[10]
    b = lst[12]
    numbers = lst[10:13]
    total = sum(set(range(a + 1, b)) - set(numbers))
    result = ''
    if total == 0:
        return result
    elif total % 2 == 0:
        result = hex(total)[2:]
    else:
        result = bin(total)[2:]
    return result