def return_binary_or_hexa(lst):
    a = lst[51]
    b = lst[76]
    missing_ints = [i for i in range(a + 1, b) if i not in lst[51:77]]
    if not missing_ints:
        return ''
    total = sum(missing_ints)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]