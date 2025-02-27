def return_binary_or_hexa(lst):
    a = lst[18]
    b = lst[60]
    total = sum((i for i in range(a + 1, b) if i not in lst))
    result = ''
    if total % 2 != 0:
        result = str(bin(total))[2:]
    else:
        result = str(hex(total))[2:].upper()
    return result