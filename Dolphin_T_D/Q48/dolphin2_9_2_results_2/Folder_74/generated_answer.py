def return_binary_or_hexa(lst):
    a = lst[69]
    b = lst[97]
    if all((i in range(a + 1, b) for i in lst[70:97])):
        return ''
    else:
        missing = [i for i in range(a + 1, b) if i not in lst[70:97]]
        total = sum(missing)
        if total % 2 == 0:
            return hex(total)[2:]
        else:
            return bin(total)[2:]