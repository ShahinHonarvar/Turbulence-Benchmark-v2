def return_binary_or_hexa(lst):
    a = lst[60]
    b = lst[90]
    if a + 1 > b - 1:
        return ''
    missing = [i for i in range(a + 1, b) if i not in lst[60:90]]
    total = sum(missing)
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]